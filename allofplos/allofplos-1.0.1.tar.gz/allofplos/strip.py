from lxml import etree
from allofplos import Corpus
import allofplos
SPACE = " ".encode("utf8")
for art in Corpus():
    def recurse(f, element):
        if element.tag is etree.Comment:
            return
        if element.text:
            f.write(SPACE)
            f.write(element.text.encode("utf8"))
            f.write(SPACE)
        for child in element:
            recurse(f, child)
        if element.tail:
            f.write(SPACE)
            f.write(element.tail.encode("utf8"))
            f.write(SPACE)
    with open("%s.txt"%(art.filepath), 'wb') as f:
        recurse(f, art.root)

