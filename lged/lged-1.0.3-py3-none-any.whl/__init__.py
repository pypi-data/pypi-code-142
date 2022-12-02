import argparse
from lged.app import App
from lged.settings import search_keys

def parse_command_line_args():
    parser = argparse.ArgumentParser(description="parse libgen.rs search parameters")
    parser.add_argument('--keyword', type=str, default=search_keys['keyword'], nargs='?', required=True,
                        help="""
                        enter search keys separated by a single space. If the keyword is more
                        than one word, wrap the keyword in double quotes.
                        """)
    parser.add_argument('--view', type=str, default=search_keys['view'], nargs='?',
                        help="""
                        enter view mode. You can check the view mode in the site.
                        The default value is "simple".
                        """)
    parser.add_argument('--page_num', type=int, default=search_keys['page_num'], nargs='?',
                        help="""
                        enter number of pages to download. The default value is 1.
                        """)
    parser.add_argument('--search_field', type=str, default=search_keys['search_field'], nargs='?',
                        help="""
                        enter search field. You can check it in the site.
                        The default value is "title".
                        """)    
    parser.add_argument('--sort', type=str, default=search_keys['sort'], nargs='?',
                        help="""
                        enter sort field. You can check the fields in the site.
                        The default value is "year".
                        """)
    parser.add_argument('--sortmode', type=str, default=search_keys['sortmode'], nargs='?',
                        help="""
                        enter sort mode: DESC or ASC. The default value is DESC.
                        """)
    parser.add_argument('--download', type=str, default=search_keys['download'], nargs='?',
                        help="""
                        enter download path. The default value is Downloads directory.
                        """)
    
    return vars(parser.parse_args())


def main():
    search_keys = parse_command_line_args()

    app = App(**search_keys)
    app.run()