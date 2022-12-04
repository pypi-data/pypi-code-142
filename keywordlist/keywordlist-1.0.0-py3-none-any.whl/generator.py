import itertools

def list_join(connectors, list_):
    if len(list_) - len(connectors) > 1:
        raise ValueError("too few connectors")
    return list_[:1] + list(itertools.chain.from_iterable(zip(connectors, list_[1:])))

class WordlistGenerator:
    def __init__(self, options: dict) -> None:
        self.keywords = options.get("keywords", tuple())
        self.max_keyword_conjunctions = options.get("max_keyword_conjunctions", 0)
        self.modifiers = options.get("modifiers", (lambda x:x,))
        self.connectors = options.get("connectors", ("",))
        self.numbers = options.get("numbers", tuple())
        self.use_numbers_as_connectors = options.get("use_numbers_as_connectors", False)

    def _generate(self):
        if self.max_keyword_conjunctions > len(self.keywords):
            raise ValueError("MAX_KEYWORD_CONJUNCTIONS must be <= len(KEYWORDS)")

        connectors_iterator = tuple(iter(self.connectors))
        if self.use_numbers_as_connectors:
            connectors_iterator = tuple(itertools.chain(self.connectors, self.numbers))
        
        for i in range(1,self.max_keyword_conjunctions+1):
            for elements in itertools.permutations(self.keywords, r=i):
                for modifiers in itertools.product(self.modifiers, repeat=i):
                    modified_elements = [changer(e) for changer,e in zip(modifiers, elements)]
                    for connectors in itertools.product(connectors_iterator, repeat=i-1):
                        candidate = "".join(list_join(connectors, modified_elements))
                        yield candidate
    
    def generate(self, unique=False):
        wordlist = self._generate()
        if unique:
            wordlist = set(wordlist)
        return list(wordlist)