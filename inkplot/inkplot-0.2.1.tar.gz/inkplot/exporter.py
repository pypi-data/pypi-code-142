import os
import tempfile

from PyPDF2 import PdfMerger

from inkplot.layered_svg import LayeredSVG
from inkplot.svg_locator import SVGLocator
from inkplot.pages import read_yaml, pagedef_expanded_pattern_visible_iterator, page_zoom_rectangle_id


class NoImageDimensions(Exception):
    pass


class InkplotExporter(object):
    """
    abstraction for generating pngs and pdfs from render definitions
    """
    render_def_filepath = None
    target = None
    _render_def = None
    _name_to_layerset_def = None

    def __init__(self, render_def_filepath, target=None):
        """
        initialize the exporter with a render definition filepath and an optional target
        """
        self.render_def_filepath = render_def_filepath
        self.target = target

    def abs_render_def_filepath(self):
        """
        this returns the absolute filename of the render definition file
        NOTE that this class should be initialized with the absolute path
        """
        return self.render_def_filepath

    def render_def(self):
        """
        returns the cached render definition data structure, reading it only
        once per initialized instance
        """
        if self._render_def:
            return self._render_def

        self._render_def = read_yaml(self.abs_render_def_filepath())
        return self._render_def

    def render_targets_iter(self):
        """
        an iterator that yields all render targets in the render definition,
        including both pdfs and images
        """
        render_def = self.render_def()
        pdf_defs = render_def.get('pdfs', [])
        for pdf_def in pdf_defs:
            yield 'pdf', pdf_def
        image_defs = render_def.get('images', [])
        for image_def in image_defs:
            yield 'image', image_def

    def name_to_layerset_def(self):
        """
        returns a dict of names to layerset definitions
        """
        if self._name_to_layerset_def:
            return self._name_to_layerset_def

        self._name_to_layerset_def = {}
        shared_layerset_defs = self.render_def()['shared']['layersets']
        for layerset_def in shared_layerset_defs:
            self._name_to_layerset_def[layerset_def['name']] = layerset_def
        return self._name_to_layerset_def

    def render_pdf(self, pdf_def):
        """
        renders a pdf using information from the pdf definition supplied as a parameter
        """
        current_dirpath = os.getcwd()
        with tempfile.TemporaryDirectory() as tmpdirname:
            os.chdir(tmpdirname)
            page_pdfs = []
            for page_def in pdf_def['pages']:

                # # read the source svg
                # svg = LayeredSVG(filepath=SVGLocator(page_def.get('source'),
                #                                      self.abs_render_def_filepath()).filepath())
                #
                # # update layer visibility
                # pattern_visibility_tuples = pagedef_expanded_pattern_visible_iterator(
                #     page_def=page_def,
                #     shared_layersets_dict=self.name_to_layerset_def())
                # for pattern, is_visible in pattern_visibility_tuples:
                #     svg.set_layer_visibility(pattern=pattern, visible=is_visible)
                #
                # # update the viewbox
                # svg.set_viewbox_to_rect(page_zoom_rectangle_id(page_def, self.render_def()['shared']['zoom-rectangles']))
                svg = self.render_svg_obj(page_def)

                page_pdf_filename = '{}.pdf'.format(page_def['name'])
                svg.write_pdf(page_pdf_filename)
                page_pdfs.append(page_pdf_filename)

            # combine the page pdfs into a final pdf
            merger = PdfMerger()
            for pdf in page_pdfs:
                merger.append(pdf)
            pdf_name = pdf_def.get('name')
            output_filepath = os.path.join(current_dirpath, f'{pdf_name}.pdf')
            merger.write(output_filepath)
            merger.close()
            os.chdir(current_dirpath)

    def render_svg_obj(self, image_or_page_def):
        # read the source svg
        svg = LayeredSVG(filepath=SVGLocator(image_or_page_def.get('source'),
                                             self.abs_render_def_filepath()).filepath())

        # update layer visibility
        pattern_visibility_tuples = pagedef_expanded_pattern_visible_iterator(
            page_def=image_or_page_def,
            shared_layersets_dict=self.name_to_layerset_def())
        for pattern, is_visible in pattern_visibility_tuples:
            svg.set_layer_visibility(pattern=pattern, visible=is_visible)

        # update the viewbox
        svg.set_viewbox_to_rect(page_zoom_rectangle_id(image_or_page_def, self.render_def()['shared']['zoom-rectangles']))
        return svg

    def render_image(self, image_def):
        """
        renders a png image using information from the image definition supplied as a parameter
        """
        svg = self.render_svg_obj(image_def)
        image_name = image_def.get('name')
        output = f'{image_name}.png'
        if ('dimensions' not in image_def or
            not('width' in image_def['dimensions'] or 'height' in image_def['dimensions'])):
            raise NoImageDimensions('image width and/or image height required')

        image_width = image_def['dimensions'].get('width')
        image_height = image_def['dimensions'].get('height')

        if not image_width:
            _, _, viewbox_width, viewbox_height = svg.viewbox()
            image_width = int(image_height * (viewbox_width / viewbox_height))

        if not image_height:
            _, _, viewbox_width, viewbox_height = svg.viewbox()
            image_height = int(image_width * (viewbox_height/viewbox_width))

        zoom_rect_id = page_zoom_rectangle_id(image_def, self.render_def()['shared']['zoom-rectangles'])

        svg.write_png(output, zoom_rect_id, image_width, image_height)

    def export(self):
        """
        export one or more targets from the render definition
        """
        for render_type, render_def in self.render_targets_iter():
            if not self.target or render_def.get('name') == self.target:
                if render_type == 'pdf':
                    self.render_pdf(render_def)
                elif render_type == 'image':
                    self.render_image(render_def)
