# Calling modest's CSS engine is expensive, and we often call it
# with the same arguments. So, try to cache things.
def _make_cached_tree_css(tree):
    tree_css_cache = {}
    def cached_tree_css(sel, node=None):
        if sel.startswith('html '):
            node = None
            sel = sel[5:]

        if node is None:
            if sel in tree_css_cache:
                return tree_css_cache[sel]

            rv = tree.css(sel)
            tree_css_cache[sel] = rv
            return rv

        key = node.attrs['data-preorder-index'] + '!' + sel
        if key in tree_css_cache:
            return tree_css_cache[key]

        rv = node.css(sel)
        tree_css_cache[key] = rv
        return rv

    return cached_tree_css


