from .selectors import _candidate_selectors, _candidate_repeating_selectors

import itertools
import time
from .equals import _node_in, _height_of
from .extract import extract_rows

def _no_banned_nodes(tree_css_func, selector, reject):
    if not reject:
        return True

    nodes = tree_css_func(selector)
    for node in reject:
        if _node_in(node, nodes):
            return False

    return True

def infer_column(tree_css_func, tree, keep, reject=[], cache={}):
    """In the given tree, propose some candidate selectors that would find elements
       that have the values in "keep". (Some massaging may be needed, eg, stripping,
       reading an attribute.)

       Don't propose a selector if it would select a node in reject."""

    sets = []

    start_time = time.time()
    for needle in keep:
        choices = []

        needle_nodes = []
        for node in tree.root.traverse():
            # To avoid wasting a ton of resource, only check nodes that have
            # 0 or 1 kids, and 
            if not node.child or not node.child.next:
                t = node.text().strip()
                if t == needle and not _node_in(node, reject):
                    choices.append((node, needle))

        if not choices:
            print('infer_column failed after ' + str(time.time() - start_time))
            return []
        sets.append(choices)

    # Create all the permutations of the sets
    permutations = list(itertools.product(*sets))

    # Try to find list of candidate selectors that find the nodes

    candidates = []
    for permutation in permutations:
        selectors = list(set.intersection(*[set(_candidate_selectors(tree, node, cache=cache)) for (node, needle) in list(permutation)]))

        # Only accept if the selector doesn't pick any of the rejected nodes.
        selectors = [selector for selector in selectors if _no_banned_nodes(tree_css_func, selector, reject)]

        if selectors:
            selectors.sort(key=lambda x: (len(x), x))
            candidates.append((permutation, selectors))

    #print(candidates)

    return candidates

def _all_at_same_height(nodes):
    if not nodes:
        return False

    height = _height_of(nodes[0])

    for node in nodes:
        if _height_of(node) != height:
            return False

    return True


def can_extract_examples(tree, row_examples, candidate_repeating_selector, ok_attribute_selectors):
    """Confirm that the output of infer can produce the examples in row_examples.

This is necessary because we do a naive (but cheap!) search for selectors that _might_
be correct; so we need to do a second pass to confirm they're correct.
"""
    optional_attrs = []
    for i in range(len(row_examples[0])):
        is_optional = False
        for j in row_examples:
            if j[i] == None:
                is_optional = True

        optional_attrs.append(is_optional)

    #print(candidate_repeating_selector + ': ' + str(ok_attribute_selectors))
    attrs = []
    for x in range(len(ok_attribute_selectors)):
        attrs.append({
            'selector': ok_attribute_selectors[x][0],
            'optional': optional_attrs[x],
            # TODO: conversions?
        })

    #print(attrs)
    extracted = extract_rows(
        tree,
        {
            'selector': candidate_repeating_selector,
            'columns': attrs
        }
    )

    for row in row_examples:
        if not row in extracted:
            return False

    return True

def infer_rows(tree, row_examples):
    cache={}

    # NB: you must have called annotate_preorder on the tree; we use the preorder indexes
    #     to cache css selector evaluations, and eventually, to prune the search space
    if not row_examples:
        raise Exception('need to provide at least one row example')

    tree_css_cache = {}
    def cached_tree_css(sel):
        if sel in tree_css_cache:
            return tree_css_cache[sel]

        rv = tree.css(sel)
        tree_css_cache[sel] = rv
        return rv

    for row_example in row_examples:
        if len(row_example) != len(row_examples[0]):
            raise Exception('all row examples should be the same length (' + str(len(row_examples[0])) + '): ' + str(row_example))

        all_empty = True
        for attr in row_example:
            if attr:
                all_empty = False

        if all_empty:
            raise Exception('at least one attribute in the row must be defined: ' + str(row_example))

    print(row_examples)

    # If an attribute is a "singleton", it means it's unique across all the examples
    # and should be computed relative to the HTML root, not relative to a repeating
    # selector. (This can cause false positives! The user will have to ensure they
    # add examples that are _not_ unique.)
    singleton_attributes = []
    optional_attributes = []

    # Pivot the row examples so instead of logical rows, we have all the birth years,
    # all the first names, etc
    attribute_examples = []
    for i in range(len(row_examples[0])):
        is_singleton = True
        all_empty = True
        some_empty = False
        attribute_examples.append([row_example[i] for row_example in row_examples])

        for x in attribute_examples[-1]:
            if x != attribute_examples[-1][0]:
                is_singleton = False

            if x:
                all_empty = False
            else:
                some_empty = True

        singleton_attributes.append(is_singleton)
        optional_attributes.append(some_empty)

        if all_empty:
            raise Exception('you must provide at least one non-null example for attribute ' + str(i))

    print(attribute_examples)

    attribute_selectors = []

    for i in range(len(attribute_examples)):

        reject = []
        #for j in range(len(attribute_examples)):
        #   if i == j:
        #       continue

        #   for needle in attribute_examples[j]:
        #       if not needle in attribute_examples[i]:
        #           reject.append(needle)

        print('! inferring from examples ' + str(attribute_examples[i]) + " (reject=" + str(reject) + ")")

        # TODO: do we need to 2 passes of infer_column? Once to find the nodes that
        #       are candidates, and a second time to exclude those nodes from the other
        #       attributes.
        selectors = infer_column(cached_tree_css, tree, [x for x in attribute_examples[i] if x], reject, cache=cache)

        if not selectors:
            raise Exception('unable to infer candidates for attribute ' + str(i) + ': ' + str(attribute_examples[i]))

        # TODO: consider deleting this; it's convenient during development to see interim things
        #       sorted by "goodness", but it'll get shaken out later, too
        for opts in selectors:
            opts[1].sort(key=lambda x: (len(x), x))

        # Ensure that singleton attributes always have 'html' style selectors
        if singleton_attributes[i]:
            for opts in selectors:
                for i in range(len(opts[1])):
                    if not opts[1][i].startswith('html '):
                        opts[1][i] = 'html ' + opts[1][i]

        attribute_selectors.append(selectors)

    # TODO/CONSIDER: exclude any selector that has only 1 example, that's a constant.

    # We may have found the example data via different selector,
    # generate all of them.

    #print(attribute_selectors)

    #print("!! attribute selectors for item code")
    #print(attribute_selectors[1])
    permutations = list(itertools.product(*attribute_selectors))

    print('! permutations')
    #print(permutations)

    candidate_selector_sets = [set() for x in row_examples[0]]
    for perm in permutations:
        # Reconstitute the examples as actual nodes
        selectors = [x[1] for x in perm]
        for i in range(len(selectors)):
            candidate_selector_sets[i] = candidate_selector_sets[i] | set(selectors[i])

    #print(permutations)

    # TODO: can we cache the set of candidate_repeating_selectors? For big documents,
    #       this can take some time (eg 1 second for mynextmake, 4.2 sec for canada computers)
    n = time.time()
    candidate_repeating_selectors = _candidate_repeating_selectors(tree, permutations, cache=cache)

    print("producing candidate_repeating_selectors took: " + str(time.time() - n))
    print("   found " + str(len(candidate_repeating_selectors)) + " candidates")

    #print(candidate_repeating_selectors)

    ok_repeating_selectors = []

    iterations_required = 0

    node_visit_count = {}
    css_cache = {}

    for candidate_repeating_selector in candidate_repeating_selectors:
        iterations_required += 1

        repeating_elements = cached_tree_css(candidate_repeating_selector)
        #print(candidate_repeating_selector + ': ' + str(len(repeating_elements)))

        # TODO: threshold should be chosen based on how many distinct examples for an
        #       attribute
        if len(repeating_elements) < 2:
            continue

        if not _all_at_same_height(repeating_elements):
            #print('bad: ' + candidate_repeating_selector)
            continue

        #print(' ok: ' + candidate_repeating_selector)

        all_attrs_ok = True
        ok_attribute_selectors = []
        for i in range(len(attribute_examples)):
            #print('! testing selectors for: ' + str(attribute_examples[i]))
            keepers = []

            for attribute_selector in candidate_selector_sets[i]:
                needed = {}
                for example in [k for k in attribute_examples[i] if k]:
                    needed[example] = True

                # If it's a singleton attribute, we should compute relative
                # to the tree root.
                search_roots = repeating_elements

                if singleton_attributes[i]:
                    search_roots = [tree.root]

                for parent in search_roots:
                    el_id = parent.attrs['data-preorder-index']
                    node_visit_count[el_id] = node_visit_count.get(el_id, 0) + 1

                    css_cache_key = el_id + '!' + attribute_selector
                    nodes = css_cache.get(css_cache_key)

                    if nodes is None:
                        nodes = parent.css(attribute_selector)
                        css_cache[css_cache_key] = nodes

                    if nodes:
                        needed.pop(nodes[0].text().strip(), 'ignore')

                if len(needed) == 0:
                    keepers.append(attribute_selector)

            if keepers:
                # prefer shorter selectors, all else being equal
                keepers.sort(key=lambda x: (len(x), x))
                #keepers = keepers[0:5]
                ok_attribute_selectors.append(keepers)
            else:
                break

        #print(ok_attribute_selectors)
        if len(ok_attribute_selectors) == len(attribute_examples):
            # Confirm we can extract the examples before accepting this selector, eg
            # we might have just found all the individual elements, but not as cohesive
            # rows
            if not can_extract_examples(tree, row_examples, candidate_repeating_selector, ok_attribute_selectors):
                continue

            ok_repeating_selectors.append((candidate_repeating_selector, ok_attribute_selectors))
            break


    ok_repeating_selectors.sort(key=lambda x: len(x[0]))
    print("performed " + str(iterations_required) + " searches")
    #print(ok_repeating_selectors[0:5])
    #print(candidate_repeating_selectors)
    print('possible solutions: ' + str(len(ok_repeating_selectors)) + ' of ' + str(len(candidate_repeating_selectors)))
    #print(node_visit_count)

    if ok_repeating_selectors:
        columns = []
        for i, x in enumerate(ok_repeating_selectors[0][1]):
            columns.append({
                'selector': x[0],
                'optional': optional_attributes[i]
            })

        return {
            'selector': ok_repeating_selectors[0][0],
            'columns': columns
        }

    return None



