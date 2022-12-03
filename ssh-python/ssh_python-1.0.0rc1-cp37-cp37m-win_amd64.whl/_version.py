
import json

version_json = '''
{"date": "2022-12-03T18:48:06.327286", "dirty": false, "error": null, "full-revisionid": "cac4dcc697f9e9562ddb7bd1a6577453da8ad5ac", "version": "1.0.0-rc1"}'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)

