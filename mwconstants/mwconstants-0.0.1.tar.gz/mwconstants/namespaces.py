import copy
import time

import requests

from mwconstants.constants.c_languages import WIKIPEDIA_LANGUAGES
from mwconstants.constants.c_namespaces import DEFAULT_NAMESPACES, NAMESPACE_ALIASES
from mwconstants.languages import get_wiki_sites


def get_all_namespace_prefix_map(lang, project='wikipedia'):
    """Get mapping of namespaces to canonical / possible aliases for a given wiki.

    For return dictionary:
    * Keys are the local names -- i.e. the official names used in parsed article HTML
    * Values include the canonical name -- e.g., User for fr:Utilisateur
    * Values include the list of possible aliases -- e.g., Utilisatrice
    * Together, the key + canonical + aliases make all the valid prefixes for a namespace

    More details: https://www.mediawiki.org/wiki/Help:Namespaces#Localisation

    NOTE: this data can alternatively be extracted from another dump:
    <lang>-<date>-siteinfo-namespaces.json.gz
    """
    session = requests.Session()
    base_url = f"https://{lang}.{project}.org/w/api.php"
    params = {
     "action": "query",
     "meta": "siteinfo",
     "siprop": "namespaces|namespacealiases",
     "format": "json",
     "formatversion": "2"
    }
    result = session.get(url=base_url, params=params)
    result = result.json()

    prefixes = {}
    id_to_name = {}  # e.g., 1 -> Talk; needed for namespace aliases
    if 'namespaces' in result.get('query', {}):
        for ns in result['query']['namespaces'].values():
            try:
                canonical = ns['canonical']
                name = ns['name']
                nid = ns['id']
                id_to_name[nid] = name
                prefixes[name] = {'canonical': canonical}
            except KeyError:  # main namespace has no canonical prefix and we want to skip it
                continue
    if 'namespacealiases' in result.get('query', {}):
        for alias in result['query']['namespacealiases']:
            try:
                nid = alias['id']
                prefix = alias['alias']
                name = id_to_name[nid]
                prefixes[name]['aliases'] = prefixes[name].get('aliases', []) + [prefix]
            except KeyError:
                print(f"Invalid alias: {alias}")

    return prefixes


def gather_all_languages(deduplicate=True):
    """Helper function for gathering namespace data of a given type."""
    wiki_languages = get_wiki_sites('wiki')
    print(f"{len(wiki_languages)} languages: {wiki_languages}")
    namespaces = {}
    for lang in wiki_languages:
        namespaces[lang] = get_all_namespace_prefix_map(lang, 'wikipedia')
        time.sleep(0.25)

    if deduplicate:
        def_ns = copy.deepcopy(namespaces['en'])
        def_canonical_to_name = {ns['canonical']: ns_name for ns_name, ns in def_ns.items()}

        langs_to_remove = []
        for lang in namespaces:
            ns_to_remove = []
            for ns_name in namespaces[lang]:
                ns = namespaces[lang][ns_name]
                # matches English exactly
                if ns == def_ns.get(ns_name):
                    ns_to_remove.append(ns_name)
                else:
                    try:
                        en_equiv = def_canonical_to_name[ns['canonical']]
                    except KeyError:
                        # Special namespaces that don't appear in English -- just remove duplicate canonical if relevant
                        if ns_name == ns['canonical']:
                            ns.pop('canonical')
                        continue
                    # remove official aliases that match any default prefixes (name/canonical/aliases)
                    def_prefixes = def_ns[en_equiv].get('aliases', []) + [en_equiv] + [def_ns[en_equiv]['canonical']]
                    for i in range(len(ns.get('aliases', [])) - 1, -1, -1):
                        if ns['aliases'][i] in def_prefixes:
                            ns['aliases'].pop(i)
                    if 'aliases' in ns and not ns['aliases']:
                        ns.pop('aliases')
                    # only keep canonical if different from name
                    if ns_name == ns['canonical']:
                        ns.pop('canonical')
                    if not ns:
                        ns_to_remove.append(ns_name)
                    elif 'aliases' not in ns and ns['canonical'] in def_prefixes and ns_name in def_prefixes:
                        ns_to_remove.append(ns_name)

            for ns in ns_to_remove:
                namespaces[lang].pop(ns)
            if not namespaces[lang]:
                langs_to_remove.append(lang)

        for lang in langs_to_remove:
            namespaces.pop(lang)

        for ns in def_ns:
            if ns == def_ns[ns]['canonical']:
                def_ns[ns].pop('canonical')

    return namespaces


def standardize_prefix(prefix):
    """Standardize link format"""
    return prefix.split(':', maxsplit=1)[0].replace(' ', '_').capitalize()


def prefixes_to_canonical(lang='en'):
    prefixes = {standardize_prefix(l):'Interlanguage' for l in WIKIPEDIA_LANGUAGES}
    for ns in DEFAULT_NAMESPACES:
        canonical = DEFAULT_NAMESPACES[ns].get('canonical', ns)
        prefixes[standardize_prefix(ns)] = canonical
        prefixes[standardize_prefix(canonical)] = canonical
        for alias in DEFAULT_NAMESPACES[ns].get('aliases', []):
            prefixes[standardize_prefix(alias)] = canonical

    for ns in NAMESPACE_ALIASES.get(lang, {}):
        canonical = NAMESPACE_ALIASES[lang][ns].get('canonical', ns)
        prefixes[standardize_prefix(ns)] = canonical
        prefixes[standardize_prefix(canonical)] = canonical
        for alias in NAMESPACE_ALIASES[lang][ns].get('aliases', []):
            prefixes[standardize_prefix(alias)] = canonical

    return prefixes


if __name__ == '__main__':
    print(gather_all_languages())  # Wikipedia namespaces
