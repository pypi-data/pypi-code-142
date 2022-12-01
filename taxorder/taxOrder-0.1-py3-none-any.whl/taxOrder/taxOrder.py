import ete3 as ete
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description='Returns list of species in a phylogenetic tree ordered '
                    'by increasing taxonomic distance to a reference species'
    )
    parser.add_argument(
        '-t', '--tree', metavar='<path>', type=str, required=True,
        help='Path to tree in Newick format'
    )
    parser.add_argument(
        '-r', '--reference', metavar='str', type=str, required=True,
        help='Reference species'
    )
    parser.add_argument(
        '--outfile', metavar='str', type=str, nargs='?', const='', default='',
        help=(
            'Save output to file'
        )
    )
    parser.add_argument(
        '--format', metavar='str', type=int, nargs='?', const=1, default=1,
        help=(
            'Tree format as specified at: \n'
            'https://etetoolkit.org/docs/latest/tutorial/tutorial_trees.html#reading-and-writing-newick-trees\n'
            '(Default: 1)'
        )
    )
    parser.add_argument(
        '--idmap', metavar='<path>', type=str, nargs='?', const='', default='',
        help=(
            'TaxOrder can map species names to taxids accepted by '
            'PhyloProfile if supplied with a tab-seperated file like:\n'
            'taxid\tname'
        )
    )

    def initial_list(t):
        copylist = []
        node = t.search_nodes(name=args.reference)[0]
        while node:
            for subnode in node:
                copylist.append(subnode.name)
            node = node.up
        return copylist

    def order_species(ilist):
        specorder = []
        for name in ilist:
            if name not in specorder:
                specorder.append(name)
        return specorder

    def parse_mappingfile(path):
        n2t = {}
        with open(path) as sh:
            for line in sh:
                taxid, name = line.strip().split()
                n2t[name] = f'ncbi{taxid}'
                if len(name.split('_')) > 2:
                    shortname = '_'.join(name.split('_')[:2])
                    n2t[shortname] = f'ncbi{taxid}'
        return n2t

    def check_file(f):
        if not os.path.isfile(f):
            raise ValueError(f'File not found at: {f}')

    args = parser.parse_args()
    for file in [args.tree, args.idmap, args.outfile]:
        if file:
            check_file(file)

    # work
    tree = ete.Tree(args.tree, format=args.format)
    initial = initial_list(tree)
    specorder = order_species(initial)
    # mapping
    if args.idmap:
        name2taxid = parse_mappingfile(args.idmap)
        outnames = [name2taxid[name] for name in specorder]
    else:
        outnames = specorder
    # output
    if args.outfile:
        with open(args.outfile, 'w') as of:
            for name in outnames:
                of.write(f'{name}\n')
    for name in outnames:
        print(name)


if __name__ == "__main__":
    main()
