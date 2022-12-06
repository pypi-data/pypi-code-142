class Collection:
    def __init__(self, items):
        self.items = items
        self.__item_count__ = len(items)
    
    def first(self):
        return self.items[0]
    
    def __len__(self):
        return self.__item_count__
