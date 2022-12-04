import songpy.music.note


class PolishNotesNamesFormatter:
    sharp = "is"
    flat = "es"
    dropped_flat_suffix_letters = {
        "C": 0,
        "D": 0,
        "E": 1,
        "F": 0,
        "G": 0,
        "A": 1,
        "B": 2
    }

    def format(self, note: songpy.music.note.Note):
        return self.base_name(note) + self.accidental_suffix(note)

    def base_name(self, note: songpy.music.note.Note):
        note_name = note.name()
        if note_name == "B" and note.accidental_modifier() >= 0:
            note_name = "H"
        return note_name

    def accidental_suffix(self, note: songpy.music.note.Note):
        modifier = note.accidental_modifier()
        if modifier > 0:
            return self.sharp_suffix(modifier)
        return self.flat_suffix(note)

    def sharp_suffix(self, semi_tones: int):
        return semi_tones * self.sharp

    def flat_suffix(self, note: songpy.music.note.Note):
        regular_suffix = - note.accidental_modifier() * self.flat
        first_index = self.dropped_flat_suffix_letters[note.name()]
        return regular_suffix[first_index:]
