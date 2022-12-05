from itertools import count


class LsDynaEntity:
    def __init__(self, keyword: str, cards: list[str]):
        self.keyword = keyword
        self.cards = tuple(cards)


def parse_entity(l_start: int, lines: list[str]) -> LsDynaEntity:
    keyword = lines[l_start].strip()
    cards = list()
    for l in count(l_start+1):
        if l==len(lines):
            break
        if lines[l].startswith('$'):
            continue
        if lines[l].startswith('*'):
            break
        cards.append(lines[l])
    return LsDynaEntity(keyword, cards)


def parse_lsdyna_deck(path: str) -> dict:
    parsed_deck = dict()
    lines = open(path).readlines()
    for l, line in enumerate(lines):
        if line.startswith('*'):
            entity = parse_entity(l_start=l, lines=lines)
            if entity.keyword in parsed_deck:
                parsed_deck[entity.keyword].append(entity)
            else:
                parsed_deck[entity.keyword] = [entity]
    return parsed_deck
