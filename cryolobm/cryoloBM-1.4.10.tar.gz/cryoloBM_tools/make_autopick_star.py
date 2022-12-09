from cryoloBM.bmtool import BMTool
import argparse
from argparse import ArgumentParser
import os
from pyStarDB import sp_pystardb as star
import pandas as pd

class MakeAutopickStar(BMTool):

    def get_command_name(self) -> str:
        return "createAutopick"

    def create_parser(self, parentparser : ArgumentParser) -> ArgumentParser:
        parser_autopick = parentparser.add_parser(
            self.get_command_name(),
            help="Scales all sort of coordinate files.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )

        autopick_required_group = parser_autopick.add_argument_group(
            "Required arguments",
            "Create Relion 4 autopick.star file.",
        )

        autopick_required_group.add_argument(
            "-m",
            "--micrographs",
            required=True,
            nargs='+',
            help="Folder to micrographs",
        )

        autopick_required_group.add_argument(
            "-c",
            "--coordinates",
            required=True,
            nargs='+',
            help="Folder to micrographs",
        )

        autopick_required_group.add_argument(
            "-o",
            "--output",
            required=True,
            help="Output folder where to write the autopick.star.",
        )

    def run(self, args):
        micrographs = args.micrographs
        coordinates = args.coordinates

        micrographs_filename = [os.path.splitext(os.path.basename(m))[0] for m in micrographs]
        coordinates_filename = [os.path.splitext(os.path.basename(m))[0] for m in coordinates]

        micrographs_mapped = []
        coordinates_mapped = []
        for m_i,m in enumerate(micrographs_filename):
            try:
                index = coordinates_filename.index(m)

                micrographs_mapped.append(os.path.realpath(micrographs[m_i]))
                coordinates_mapped.append(os.path.realpath(coordinates[index]))
            except ValueError:
                print("Did not found matching coordinate file for ", m)
        data_dict = {'_rlnMicrographName': micrographs_mapped, '_rlnMicrographCoordinates': coordinates_mapped}
        data = pd.DataFrame(data_dict)
        os.makedirs(args.output,exist_ok=True)
        new_sfile = star.StarFile(os.path.join(args.output,"autopick.star"))
        new_sfile.update('coordinate_files', data, loop=True)
        new_sfile.write_star_file(overwrite=True)



        pass