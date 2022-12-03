from parsing_utils import process_kanjidic_node, process_jmdict_node, ParsingBase


class KanjidicParser(ParsingBase):
    def _modify_offset(self):
        self.offset = 1

    def _parse_elem(self, elem, logger):
        return process_kanjidic_node(elem)


class JmdictParser(ParsingBase):
    def _modify_offset(self):
        self.offset = 0

    def _parse_elem(self, elem, logger):
        return process_jmdict_node(elem)
