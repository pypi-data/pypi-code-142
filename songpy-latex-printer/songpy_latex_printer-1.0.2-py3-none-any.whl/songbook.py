# songbook-latex -- python package for generating formatted songs with chords in LaTeX
# Copyright (C) 2022  Karol Ważny

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import unicodedata
from io import BytesIO, StringIO
import importlib.resources

import songpy
from songpy.music.chord import Chord

from latexprinter.utils import insert_at


class Generator:
    song_part_type_mappings = {
        "verse": "verse",
        "chorus": "chorus"
    }
    song_part_options = {
        "verse": "",
        "chorus": "[format=\itshape]"
    }

    def __init__(self, chord_formatter):
        self.text = None
        self.chord_formatter = chord_formatter

    def generate(self, songbook: songpy.SongBook, target_stream=None):
        self.text = ""
        self.write_preamble()
        for song in songbook.songs:
            self.write_song(song)
        self.write_postamble()
        self.normalize_unicode()
        if target_stream is None:
            target_stream = StringIO()
        target_stream.write(self.text)
        return target_stream

    def write_preamble(self):
        preamble_file = importlib.resources.files("latexprinter.resources").joinpath("preamble.txt").open()
        self.text += preamble_file.read()

    def write_postamble(self):
        preamble_file = importlib.resources.files("latexprinter.resources").joinpath("postamble.txt").open()
        self.text += preamble_file.read()

    def write_song(self, song):
        self.start_song(song.title)
        for song_part in song.content:
            self.write_song_part(song_part)
        self.end_song()

    def start_song(self, title):
        self.text += "\n\\begin{song}{title={" + title + "}}"

    def end_song(self):
        self.text += "\n\\end{song}"

    def write_song_part(self, song_part):
        self.start_song_part(song_part)
        self.text += " \\\\\n".join([self.build_line(line) for line in song_part.content])
        self.end_song_part(song_part)

    def build_line(self, song_line):
        return "".join([self.make_atom(atom) for atom in song_line.content])

    def make_atom(self, atom):
        printed_chord = "" if atom.chord is None else "{" + self.format_chord(atom.chord) + "}"
        printed_text = str(atom.text)
        first_space = printed_text.find(" ")
        if printed_chord != "":
            if first_space > 3 or first_space < 0:
                printed_text = insert_at(printed_text, " ", 3)
                printed_chord = "^*" + printed_chord
            else:
                printed_chord = "^" + printed_chord
        return printed_chord + printed_text

    def format_chord(self, chord: Chord) -> str:
        return self.chord_formatter.format(chord)

    def start_song_part(self, songpart):
        marked_indicator = "" if songpart.marked else "*"
        self.text += ("\n\\begin{" + self.song_part_type_mappings[songpart.type] + marked_indicator + "}"
                      + self.song_part_options[songpart.type] + "\n")

    def end_song_part(self, songpart):
        marked_indicator = "" if songpart.marked else "*"
        self.text += "\n\\end{" + self.song_part_type_mappings[songpart.type] + marked_indicator + "}"

    def normalize_unicode(self):
        self.text = unicodedata.normalize("NFC", self.text)


class ChordFormatter:
    suffixes = {
        Chord.Mode.MINOR: "mi",
        Chord.Mode.MAJOR: ""
    }

    def __init__(self, note_formatter):
        self.note_formatter = note_formatter

    def format(self, chord: Chord) -> str:
        return self.root_name(chord) + self.mode_suffix(chord)

    def mode_suffix(self, chord: Chord) -> str:
        return self.suffixes[chord.mode()]

    def root_name(self, chord: Chord) -> str:
        return self.note_formatter.format(chord.root())
