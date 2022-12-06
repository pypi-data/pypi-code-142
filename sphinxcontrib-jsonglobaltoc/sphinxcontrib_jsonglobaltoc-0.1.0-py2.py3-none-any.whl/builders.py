from typing import Dict, Any
from sphinxcontrib.serializinghtml import JSONHTMLBuilder
from sphinx.environment.adapters.toctree import TocTree


class SphinxGlobalTOCJSONHTMLBuilder(JSONHTMLBuilder):

    name: str = 'json'

    def get_doc_context(self, docname: str, body: str, metatags: str) -> Dict[str, Any]:
        """
        Extends :py:class:`sphinxcontrib.serializinghtml.JSONHTMLBuilder`.

        Add a ``globaltoc`` key to our document that contains the HTML for the
        global table of contents.
        """
        doc = super().get_doc_context(docname, body, metatags)
        self_toctree = TocTree(self.env).get_toctree_for(docname, self, True)
        toctree = self.render_partial(self_toctree)['fragment']
        doc['globaltoc'] = toctree
        return doc
