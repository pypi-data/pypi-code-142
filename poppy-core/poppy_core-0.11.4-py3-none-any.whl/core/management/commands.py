import logging
import importlib
import os
import shutil
import stat
import sys
from datetime import datetime
from os import path
from pprint import pformat
import declic as cli
from sqlalchemy import UniqueConstraint

import jinja2
import poppy.core as poppy_core

logger = logging.getLogger('poppy-cli')


def render(template_filepath, context):
    template_path, filename = os.path.split(template_filepath)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_path or './')
    ).get_template(filename).render(context)


def make_writeable(filename):
    """
    Make sure that the file is writeable.
    Useful if our source is read-only.
    """
    if sys.platform.startswith('java'):
        # On Jython there is no os.access()
        return
    if not os.access(filename, os.W_OK):
        st = os.stat(filename)
        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
        os.chmod(filename, new_permissions)


def create_from_template(pipeline_or_plugin, name, directory, namespace=None):
    """
    Create pipeline/plugin directory tree from POPPy templates

    :param pipeline_or_plugin: String indicating which template to use ('pipeline' or 'plugin')
    :param name: name of the pipeline/plugin
    :param directory: path to the plugin/pipeline directory
    :return:
    """
    base_subdir = '%s_template' % pipeline_or_plugin

    # store the template dir path
    template_dir = path.join(poppy_core.__path__[0], 'management', 'templates', base_subdir)

    prefix_length = len(template_dir) + 1

    # if some directory is given, make sure it's nicely expanded
    if directory is None:
        top_dir = path.join(os.getcwd(), name)
        try:
            os.makedirs(top_dir)
        except FileExistsError:
            raise FileExistsError("'%s' already exists" % top_dir)
        except OSError as e:
            raise OSError(e)
    else:
        top_dir = os.path.abspath(path.expanduser(directory))
        if not os.path.exists(top_dir):
            raise FileNotFoundError("Destination directory '%s' does not "
                                    "exist, please create it first." % top_dir)

    base_name = '%s_name' % pipeline_or_plugin
    base_directory = '%s_directory' % pipeline_or_plugin
    camel_case_name = 'camel_case_%s_name' % pipeline_or_plugin
    camel_case_value = ''.join(x for x in name.title() if x != '_')
    databases = [
        {
            "identifier": "MAIN-DB",
            "short_identifier": 'MAIN-DB',
            "vendor": "postgresql",
            "connector": "poppy.pop.db_connector.POPPy",
            "name": "poppy_tuto",
            "host": "localhost",
            "admin_account": "pipeadmin",
            "admin_password": "adminpwd",
            "user_account": "pipeuser",
            "user_password": "userpwd",
            "short_description": "POPPy tutorial database",
            "description": "POPPy tutorial Database",
            "release": {
                       "author": "POPPy team",
                       "date": "2018-06-26",
                       "institute": "LESIA",
                       "reference": "POPPy_Framework_User_Manual",
                       "version": "0.1.0",
                       "modification": ""
                       }
        }
    ]

    context = {
        base_name: name,
        base_directory: top_dir,
        camel_case_name: camel_case_value,
        'plugin_namespace': namespace,
        'poppy_core_version': poppy_core.__version__,
        'provider': 'LESIA',
        'release_date': datetime.utcnow().strftime('%Y-%m-%d'),
        'databases': databases,
        'databases_with_description': [x for x in databases if 'description' in x]
    }

    logger.debug('context: %s' % pformat(context))

    for root, dirs, files in os.walk(template_dir):

        path_rest = root[prefix_length:]

        # create relative filepath
        if namespace is not None:
            relative_dir = path_rest.replace('plugin_namespace', namespace).replace(base_name, name)
        else:
            relative_dir = path_rest.replace(base_name, name)
        if relative_dir:
            target_dir = path.join(top_dir, relative_dir)
            if not path.exists(target_dir):
                os.mkdir(target_dir)

        # ignore pycache and hidden directories
        for dir_name in dirs[:]:
            if dir_name.startswith('.') or dir_name == '__pycache__':
                dirs.remove(dir_name)

        for filename in files:
            if filename.endswith(('.pyo', '.pyc', '.py.class')):
                # ignore some files as they cause various breakages.
                continue
            old_path = path.join(root, filename)
            if filename[-4:] == '-tpl':
                new_filename = filename[:-4]
            else:
                new_filename = filename

            new_path = path.join(top_dir, relative_dir,
                                 new_filename.replace(base_name, name))

            if path.exists(new_path):
                raise FileExistsError("%s already exists, overlaying a "
                                      "project or app into an existing "
                                      "directory won't replace conflicting "
                                      "files" % new_path)

            if filename[-4:] == '-tpl':
                content = render(old_path, context)
                with open(new_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(content)
            else:
                shutil.copyfile(old_path, new_path)

                logger.debug("Creating %s\n" % new_path)
            try:
                shutil.copymode(old_path, new_path)
                make_writeable(new_path)
            except OSError:
                logger.error("Notice: Couldn't set permission bits on %s. You're "
                             "probably using an uncommon filesystem setup. No "
                             "problem." % new_path)


def setup_logger(quiet, debug):

    # set logger formatter
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # set logging level
    if debug:
        logger.setLevel(logging.DEBUG)
    elif quiet:
        logger.setLevel(logging.WARNING)
    else:
        logger.setLevel(logging.INFO)

    logging_level = logging.getLevelName(logger.getEffectiveLevel())
    logger.debug('Logging level: %s' % logging_level)


@cli.group(on_before=setup_logger)
@cli.argument('--version', action='version', version=poppy_core.__version__)
@cli.argument('-q', '--quiet', action='store_true')
@cli.argument('-d', '--debug', action='store_true')
def poppy_cli():
    pass


@poppy_cli.group()
def create():
    pass


@create.command(description='Create a new pipeline', chain=True)
@cli.argument('name', help='Name of the pipeline')
@cli.argument('--directory', help='Optional destination directory')
def pipeline(name, directory):
    create_from_template('pipeline', name, directory)


@create.command(description='Create a new plugin', chain=True)
@cli.argument('name', help='Name of the plugin')
@cli.argument('--directory', help='Optional destination directory')
@cli.argument('--namespace', help='Plugin namespace')
@cli.argument('--cython', action='store_true', help='Create a Cython-ready plugin')
def plugin(name, directory, namespace, cython):
    if name.count('.') > 1:
        raise ValueError(f'{name} has more than one \'dot\' character')

    if '.' in name:
        split_name = name.split('.')
        namespace = split_name[0]
        name = split_name[1]

    if namespace is None:
        # FIXME
        raise NotImplementedError('Plugins without namespace are not yet supported')

    create_from_template('plugin', name, directory, namespace)


@poppy_cli.command(description='Generate the database documentation of a plugin')
@cli.argument('plugin_name', help='The name of the plugin we want to generate the documentation of')
def gen_doc(plugin_name):
    """
    This function generate an reST file in the current directory. This file
    contains the model documentation about a given plugin.
    """

    plugin_models = importlib.import_module(f'{plugin_name}.models')
    try:
        tables = plugin_models.tables
    except AttributeError:
        raise AttributeError('Are you sure you have included the mandatory code '
                             'to your plugin.models.__init__.py ? See the '
                             'poppy documentation about models.')

    file_name = f'{plugin_name}_model_documentation.rst'
    file_path = os.path.join(os.path.curdir, file_name)

    csv_table_header = '.. csv-table:: {0}\n' \
                       '   :header: "Column name", "Data type", "Description", ' \
                       '"Priority", "Comment"\n\n'

    with open(file_path, 'w') as f:

        # A dictionary containing schema name as key, and all the generated text
        # of the tables in each schema as value
        table_doc_dict = dict()

        for table_name, model_class in tables.items():

            text = ''
            schema_name = 'public'

            # Title of the section
            title = f'The table {table_name}\n'
            text += title
            text += f"{'='*(len(title)-1)}\n"

            # The docstring of the class representation of the table
            text += ' '.join(model_class.__doc__.replace('\n', '').split()) # Replaces sequences of space with one and remove linebreaks
            text += '\n\n'

            text += csv_table_header.format(table_name)

            for c in model_class.__table__.columns:
                col_infos = c.infos()
                text += f'   "{col_infos["name"]}", "{col_infos["sql_type"]}", "{col_infos["description"]}", "{col_infos["priority"]}", "{col_infos["comment"]}"\n'

            text += '\n'

            table_args = model_class.__table_args__

            # Extract unique constraints and schema name (if any)
            if type(table_args) == tuple:
                for arg in table_args:
                    if type(arg) == UniqueConstraint:
                        constraint = arg
                        columns = '(' + ','.join([x.key for x in constraint]) + ')'
                        text += f'The tuple of columns {columns} must be unique.\n'
                    elif type(arg) == dict:
                        try:
                            schema_name = arg['schema']
                        except KeyError:
                            pass

            elif type(table_args) == dict:
                try:
                    schema_name = table_args['schema']
                except KeyError:
                    pass

            text += '\n'

            try:
                table_doc_dict.update({schema_name:table_doc_dict[schema_name]+text})
            except KeyError:
                table_doc_dict.update({schema_name:text})


        for schema_name, text in table_doc_dict.items():

            schema_header = f'The \'{schema_name}\' schema\n'

            f.write(f"{'*'*(len(schema_header)-1)}\n")
            f.write(schema_header)
            f.write(f"{'*'*(len(schema_header)-1)}\n\n")

            f.write(table_doc_dict[schema_name])



    logger.info(f'{file_name} successfully generated in the current directory')


if __name__ == '__main__':
    poppy_cli()
