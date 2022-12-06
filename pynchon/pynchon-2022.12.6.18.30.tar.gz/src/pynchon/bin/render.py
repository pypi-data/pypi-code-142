""" pynchon.bin.render
"""
import yaml 
import pynchon
from pynchon import (util,)
from .common import kommand
from pynchon.bin import (groups, options)
LOGGER = pynchon.get_logger(__name__)
PARENT=groups.render
import click
import os
import json
import pyjson5

files_arg = click.argument('files', nargs=-1)

def _rj5(file, output='', in_place=False):
    """ """
    LOGGER.debug(f"Running with one file: {file}")
    with open(file, 'r') as fhandle:
        data = pyjson5.loads(fhandle.read())
    if in_place:
        assert not output,'cannot use --in-place and --output at the same time'
        output = os.path.splitext(file)[0]
        output = f'{output}.json'
    if output:
        with open(output,'w') as fhandle:
            content = json.dumps(data)
            fhandle.write(f"{content}\n")
    return data

def _render(text:str='', context:dict={}):
    """
    """
    return text

def _rj2(file, output='', in_place=False, ctx={}):
    """ """
    LOGGER.debug(f"Running with one file: {file}")
    with open(file, 'r') as fhandle:
        content = fhandle.read()
    if in_place:
        assert not output,'cannot use --in-place and --output at the same time'
        output = os.path.splitext(file)
        if output[-1]=='.j2':
            output = output[0]
        else:
            output = ''.join(output)
    if not isinstance(ctx, (dict,)):
        ext = os.path.splitext(ctx)[-1]
        if ext in ['json']:
            LOGGER.debug(f"context is json file @ `{ctx}`")
            with open(ctx,'r') as fhandle:
                ctx = json.loads(fhandle.read())
        else:
            LOGGER.critical(f"unrecognized extenson for context file: {ext}")
            raise TypeError(ext)
    if output:
        with open(output, 'w') as fhandle:
            content = _render(text=content, context=ctx)
            fhandle.write(f"{content}\n")
    return content

@kommand(
    name='json5', parent=PARENT,
    # formatters=dict(),
    options=[
        options.file,
        options.stdout,
        options.output,
        click.option(
            '--in-place', is_flag=True, default=False,
            help=('if true, writes to {file}.json (dropping any other extensions)')),
    ],
    arguments=[files_arg],)
def render_json5(file, files, stdout, output, in_place):
    """
    Render render JSON5 files -> JSON
    """
    assert (file or files) and not (file and files), 'expected files would be provided'
    if file:
        return _rj5(file, output=output, in_place=in_place)
    elif files:
        # files = files.split(' ')
        LOGGER.debug(f"Running with many: {files}")
        return [
            _rj5(file, output=output, in_place=in_place)
            for file in files ]

@kommand(
    name='any', parent=PARENT,
    formatters=dict(
        # markdown=pynchon.T_TOC_CLI,
    ),
    options=[
        options.file,
        options.format,
        options.stdout,
        options.output,])
def render_any(format, file, stdout, output):
    """
    Render files with given renderer
    """
    print('hello world')

@kommand(
    name='jinja', parent=PARENT,
    options=[
        options.file,
        options.ctx,
        options.stdout,
        options.output,
        click.option(
            '--in-place', is_flag=True, default=False,
            help=('if true, writes to {file}.{ext} (dropping any .j2 extension if present)')),
    ],
    arguments=[files_arg],)
def render_j2(file, files, ctx, stdout, output, in_place):
    """
    Render render J2 files with given context
    """
    assert (file or files) and not (file and files), 'expected files would be provided'
    if ctx:
        if '{' in ctx:
            LOGGER.debug("context is inlined JSON")
            ctx = {}
        elif '=' in ctx:
            LOGGER.debug("context is inlined (comma-separed k=v format)")
            ctx = {}
        else:
            with open(ctx,'r') as fhandle:
                content = fhandle.read()
            if ctx.endswith('.json'):
                ctx = json.loads(content)
            elif ctx.endswith('.json5'):
                ctx = pyjson5.loads(content)
            elif ctx.endswith('.yml') or ctx.endswith('.yaml'):
                ctx = yaml.loads(content)
            else:
                raise TypeError(f'not sure how to load: {ctx}')
    else:
        ctx = {}
    if file:
        return _rj2(file, ctx=ctx, output=output, in_place=in_place)
    elif files:
        LOGGER.debug(f"Running with many: {files}")
        return [
            _rj2(file, output=output, in_place=in_place)
            for file in files ]

# @kommand(
#     name='version', parent=PARENT,
#     # FIXME: formatters=dict(markdown=pynchon.T_VERSION_METADATA),
#     options=[
#         # FIXME: options.output_with_default('docs/VERSION.md'),
#         options.format_markdown,
#         options.stdout, options.header])
# def version(format, file, stdout, output, header):
#     """
#     Describes version details for package (and pynchon itself).
#     """
#     return dict(
#         pynchon_version='..',
#         package_version='..',
#         git_hash='..', )
