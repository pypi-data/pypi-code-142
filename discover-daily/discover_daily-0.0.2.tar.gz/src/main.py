import argparse
import random
import json
import webbrowser


def recommend_album():
    with open('./albums.json') as f:
        albums = json.load(f)

    random_album = albums[random.randrange(0, len(albums) - 1)]

    parser = argparse.ArgumentParser(description='CLI tool recommending you an album from the RYM Charts. 365 should be enough, eh?')
    parser.add_argument(
        "-y",
        "--youtube",
        help="Opens up YouTube and searches for the album",
        action="store_true"
    )

    args = parser.parse_args()

    print(
        f"The album of the day is {random_album['album']} from {random_album['artist']}. The album has a rating of {random_album['rating']} and was released {random_album['release_date']}")

    if args.youtube:
        webbrowser.open(
            f'https://www.youtube.com/results?search_query={random_album["album"].replace(" ", "+")}+{random_album["artist"].replace(" ", "+")}')
