import time

import requests

from mwconstants.languages import get_wiki_sites


def get_valid_img_options(lang):
    """Get official list of acceptable image formatting tags -- e.g., frameless, top, etc."""
    session = requests.Session()
    base_url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "meta": "siteinfo",
        "siprop": "magicwords",
        "format": "json",
        "formatversion": "2",
    }
    result = session.get(url=base_url, params=params)
    result = result.json()

    img_keywords = []
    img_param_names = []
    img_startswith = []
    img_endswith = []
    if "magicwords" in result.get("query", {}):
        for magic in result["query"]["magicwords"]:
            if magic['name'].startswith('img_'):
                if not magic['case-sensitive']:
                    # we don't handle case insensitive so...
                    print(f"warning case-insensitive for {lang}: {magic}")
                for tag in magic['aliases']:
                    if '=' in tag:
                        img_param_names.append((magic['name'], tag.split('=')[0]))
                    elif tag.endswith('$1'):
                        img_startswith.append((magic['name'], tag[:-2]))
                    elif tag.startswith('$1'):
                        img_endswith.append((magic['name'], tag[2:]))
                    elif '$' in tag:
                        print("Didn't expect this:", tag)
                    else:
                        img_keywords.append((magic['name'], tag))
    return {'keywords': set(img_keywords),
            'params': set(img_param_names),
            'startswith': set(img_startswith),
            'endswith': set(img_endswith)}


def get_img_options(project='wiki'):
    """
    Utility for generating language-specific lists of valid media formatting options on a Wikimedia project.

    For example, to know that [[File:image.png|thumb]] has `thumb` formatting as opposed to a caption that reads `thumb`
    we must know that `thumb` is a valid image formatting tag and appears as a stand-alone keyword. Any parameters that
    do not match a valid image formatting tag pattern are assumed to be the image caption.

    See: https://www.mediawiki.org/wiki/Help:Images#Syntax
    """

    wiki_languages = get_wiki_sites(project)
    print(f"{len(wiki_languages)} languages: {wiki_languages}")
    img_options = {}
    for lang in wiki_languages:
        img_options[lang] = get_valid_img_options(lang)
        time.sleep(0.25)

    # set -> list: lists are short enough that lookups still quite fast
    for lang in img_options:
        for param_type in img_options[lang]:
            img_options[lang][param_type] = sorted(img_options[lang][param_type])

    # separate out english tags, which are valid for any language
    # this greatly reduces the size of the final list
    default_option_tags = img_options['en']

    to_remove = []
    for lang in img_options:
        for param_type in default_option_tags:
            for tag in default_option_tags[param_type]:
                img_options[lang][param_type].remove(tag)
            if not img_options[lang][param_type]:
                img_options[lang].pop(param_type)
        if not img_options[lang]:
            to_remove.append(lang)

    for lang in to_remove:
        img_options.pop(lang)

    return default_option_tags, img_options


if __name__ == "__main__":
    print(get_img_options('wiki'))  # Wikipedia image formatting options
