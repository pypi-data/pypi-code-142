import os, sys, csv
csv.field_size_limit(sys.maxsize)

def main(args):
    if len(args) < 2:
        sys.stderr.write('2 required arguments: <input csv file> <output csv path>\n')
        sys.exit(-1)

    of = open(args[1], 'wt')

    with open(args[0], 'rt') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            label = row[0]
            text = row[1].rstrip().replace('\n', ' <cr> ')
            of.write('%s\t%s\n' % (label, text))

if __name__ == '__main__':
    main(sys.argv[1:])