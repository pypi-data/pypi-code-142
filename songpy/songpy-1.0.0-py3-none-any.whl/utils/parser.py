import json
import re

from songpy.music.chord import Chord
from songpy.song import OneChordAtom, SongPart, Song, SongLine, SongBook
from songpy.utils import PolishNoteNamesPreprocessor
from songpy.utils.transpose import transpose_by_semitones

PREPROCESSORS_CHAIN = []
SONG_PART_MARKERS = [
    "^[0-9]+\\.\\s*",
    "^ref(ren|((\\.)?)):?\\s*"
]


def register_preprocessor(preprocessor):
    PREPROCESSORS_CHAIN.append(preprocessor)


def is_marked(dictionary: dict) -> bool:
    for marker_pattern in SONG_PART_MARKERS:
        if bool(re.search(marker_pattern, dictionary['content'][0], flags=re.IGNORECASE)):
            return True
    return False


def strip_markers(line: str) -> str:
    result = line
    for marker_pattern in SONG_PART_MARKERS:
        result = re.sub(marker_pattern, "", result, flags=re.IGNORECASE)
    return result


def preprocess_line(raw: str) -> str:
    product = raw
    for preprocessor in PREPROCESSORS_CHAIN:
        product = preprocessor.process(product)
    return product


def song_part_from_dictionary(dictionary: dict) -> SongPart:
    raw_lines = dictionary['content'].strip().split('\n')
    should_be_marked = is_marked({'content': raw_lines})
    if should_be_marked:
        raw_lines[0] = strip_markers(raw_lines[0])
    lines = list(map(parse_line, raw_lines))
    return SongPart(content=lines, type=dictionary['type'], marked=should_be_marked)


def parse_line(raw: str) -> [OneChordAtom]:
    product = preprocess_line(raw)
    pattern = r'(\[([^\]]*)\])?' + r'([^\[]*)'
    matches = re.finditer(pattern, product)
    return SongLine([OneChordAtom(text=match.group(3), chord=Chord.from_symbol(match.group(2)))
                     for match in matches][:-1])


def song_from_dictionary(dictionary: dict) -> Song:
    output = Song(dictionary['title'])
    output.lyrics_author = dictionary['lyrics']
    output.music_author = dictionary['music']
    # output.translation_author = dictionary['translated']
    content = dictionary['content']
    for song_part in content:
        output.add_song_part(song_part_from_dictionary(song_part))
    if 'transposition' in dictionary:
        output = transpose_by_semitones(output, dictionary['transposition'])
    if 'truncation' in dictionary:
        output.content = output.content[:dictionary['truncation']]
    return output


def songbook_from_dictionary(dictionary: dict) -> SongBook:
    output = SongBook()
    song_dicts = dictionary
    for song_dict in song_dicts:
        output.songs.append(song_from_dictionary(song_dict))
    output.sort_songs()
    return output


class SimplePrinter:
    @classmethod
    def print(cls, song: Song) -> str:
        output = song.title
        verse_count = 1
        for part in song.content:
            output += "\n"
            prefix = ""
            if part.marked:
                if part.type == 'chorus':
                    prefix = "Ref.: "
                if part.type == 'verse':
                    prefix = str(verse_count) + ". "
                    verse_count += 1
                output += prefix
            for line in part.content:
                output += line.lyrics() + " | " + " ".join(list(map(simple_printer, line.chords())))
                output += "\n"
        return output


def simple_printer(obj) -> str:
    return str(obj)


if __name__ == '__main__':
    register_preprocessor(PolishNoteNamesPreprocessor())
    file = open("song.json", 'r')
    song = json.load(file)
    file.close()
    song = song_from_dictionary(song)
    print(SimplePrinter().print(song))
