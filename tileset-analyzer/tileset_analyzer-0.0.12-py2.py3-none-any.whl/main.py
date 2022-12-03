


from tileset_analyzer.api.main_api import start_api
from tileset_analyzer.data_source.tile_source_factory import TilesetSourceFactory
from tileset_analyzer.utils.json_utils import write_json_file
import sys

OUTPUT_JSON = 'ui/data/analysis_result.json'


def execute(src_path):
    print('processing started')

    data_source = TilesetSourceFactory.get_tileset_source(src_path)
    result = data_source.analyze()

    write_json_file(result.get_json(), OUTPUT_JSON)
    print('processing completed')

    print('Web UI started')
    start_api()
    print('Web UI stopped')



def cli():
    
    print('input:')
    print(sys.argv)
    print('------------------')
    src_path = None
    if '--source' in sys.argv[1:]:
        print(sys.argv)
        source_index = sys.argv.index('--source')
        src_path = sys.argv[source_index + 1]
    else:
        print('invalid Input.. Missing --source argument')
        exit(0)

    execute(src_path)



'''
if __name__ == "__main__":
   cli()
'''
