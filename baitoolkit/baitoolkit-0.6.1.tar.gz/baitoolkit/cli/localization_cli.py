# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import os

import click


@click.group()
def localization_group():
    """Create and update localization messages."""


@localization_group.command(name='init')
@click.option('-d', '--directory', default='translations', help='Locale directory of babel.')
@click.option('-l', '--locale', default='zh_Hans_CN', help='babel default locale.', show_default=False)
def init(directory, locale):
    """Init localization messages pot."""
    if os.system(
            'pybabel extract -F %s/babel.cfg --no-default-keywords -k _ -k t_ -k l_ -o %s/messages.pot --input-dir=.' %
            (directory, directory)):
        raise RuntimeError('Failed to extract.')
    if os.system('pybabel init -i %s/messages.pot -d %s -l %s' %
                 (directory, directory, locale)):
        raise RuntimeError('Failed to init.')
    os.remove('%s/messages.pot' % directory)


@localization_group.command(name='update')
@click.option('-d', '--directory', default='translations', help='Locale directory of babel.')
def update(directory):
    """Update localization messages."""
    if os.system(
            'pybabel extract -F %s/babel.cfg --no-default-keywords -k _ -k t_ -k l_ -o %s/messages.pot .' %
            (directory, directory)):
        raise RuntimeError('Failed to extract.')
    if os.system(
            'pybabel update -i %s/messages.pot -d %s' %
            (directory, directory)):
        raise RuntimeError('Failed to update.')
    os.remove('%s/messages.pot' % directory)


@localization_group.command(name='compile')
@click.option('-d', '--directory', default='translations', help='Locale directory of babel.')
def compile_locale_message(directory):
    """Compile localization messages."""
    if os.system('pybabel compile -d %s' % directory):
        raise RuntimeError('Failed to compile')