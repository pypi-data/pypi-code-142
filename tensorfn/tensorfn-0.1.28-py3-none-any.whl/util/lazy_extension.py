class LazyExtension:
    def __init__(self, name, sources):
        from torch.utils import cpp_extension

        self.cpp_ext = cpp_extension

        self.name = name
        self.sources = sources
        self.loaded = False
        self.extension = None

    def get(self):
        if self.extension is None:
            self.extension = self.cpp_ext.load(self.name, sources=self.sources)

        return self.extension
