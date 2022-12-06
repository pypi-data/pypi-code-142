""" pynchon.bin.project
"""
import pynchon
from pynchon import (util,)
from .common import kommand
from pynchon.bin import (groups, options)
LOGGER = pynchon.get_logger(__name__)
PARENT=groups.project
@kommand(
    name='entrypoints', parent=PARENT,
    formatters=dict(markdown=pynchon.T_TOC_CLI),
    options=[ options.file_setupcfg, options.format,
        options.stdout, options.output, options.header])
def project_entrypoints(format, file, stdout, output, header):
    """
    Describe entrypoints for this project (parses setup.cfg)
    """
    return util.load_entrypoints(
            util.load_setupcfg(file=file))


@kommand(
    name='version', parent=PARENT,
    # FIXME: formatters=dict(markdown=pynchon.T_VERSION_METADATA),
    options=[
        # FIXME: options.output_with_default('docs/VERSION.md'),
        options.format_markdown,
        options.stdout, options.header])
def version(format, file, stdout, output, header):
    """
    Describes version details for package (and pynchon itself).
    """
    return dict(
        pynchon_version='..',
        package_version='..',
        git_hash='..', )
