# how could this be published to take the schema from the local filesystem?
# should have some w3id redirection and not use such a long url
# from pprint import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper


def print_nt():
    gh_schema_url = \
        "https://raw.githubusercontent.com/microbiomedata/cleanroom-schema/main/src/cleanroom_schema/schema/cleanroom_schema.yaml"

    schema_view = SchemaView(gh_schema_url)

    nt = schema_view.get_class("NamedThing")

    print(yaml_dumper.dumps(nt))
