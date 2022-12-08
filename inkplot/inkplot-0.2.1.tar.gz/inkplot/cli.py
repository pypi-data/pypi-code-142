import click
from inkplot.exporter import InkplotExporter
from inkplot.svg_locator import SVGLocator


@click.command()
@click.argument('render_def')
@click.option('--single-target', default=None, help='the name of the item to export, pdf or image')
def inkplot(render_def, single_target):
    SVGLocator.set_call_dirpath()

    exporter = InkplotExporter(render_def_filepath=render_def, target=single_target)
    exporter.export()
