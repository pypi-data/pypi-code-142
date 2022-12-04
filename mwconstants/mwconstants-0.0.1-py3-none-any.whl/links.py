from mwconstants.namespaces import prefixes_to_canonical, standardize_prefix


def standardize_link(link_title):
    """Standardize link format"""
    return link_title.replace(' ', '_').capitalize()


def link_to_namespace(link_title, lang='en', prefix_map=None):
    """Get prefix name (or None if article namespace) for a link."""
    if prefix_map is None:
        prefix_map = prefixes_to_canonical(lang=lang)
    return prefix_map.get(standardize_prefix(link_title))
