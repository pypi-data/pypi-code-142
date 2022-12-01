#!/usr/bin/env python3

import sys
import argparse

from mstk.forcefield import ForceField


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='+', type=str, help='force field files')
    parser.add_argument('-o', '--output', required=True, type=str, help='output file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    ff = ForceField.open(*args.input)
    print('%6i atom types\n'
          '%6i virtual site terms\n'
          '%6i self vdW terms\n'
          '%6i pairwise vdW terms\n'
          '%6i charge increment terms\n'
          '%6i bond terms\n'
          '%6i angle terms\n'
          '%6i dihedral terms\n'
          '%6i improper terms\n'
          '%6i polarizable terms' % (
              len(ff.atom_types), len(ff.virtual_site_terms), len(ff.vdw_terms), len(ff.pairwise_vdw_terms),
              len(ff.qinc_terms), len(ff.bond_terms), len(ff.angle_terms),
              len(ff.dihedral_terms), len(ff.improper_terms), len(ff.polarizable_terms)
          ))

    ff.write(args.output)
