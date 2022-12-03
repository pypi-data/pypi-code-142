
import json

version_json = '''
{"date": "2022-12-03T21:21:29.968237", "dirty": false, "error": null, "full-revisionid": "a62aaf26aa18b861242364ddf3c18bc5d8343ae6", "version": "1.0.0"}'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)

