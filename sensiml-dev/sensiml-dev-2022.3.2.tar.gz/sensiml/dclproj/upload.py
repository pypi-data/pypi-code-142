import json
import os

from sensiml.datamanager.label import Label
from sensiml.datamanager.labelvalue import LabelValue
from sensiml.datamanager.metadata import Metadata
from sensiml.datamanager.metadata_relationship import MetadataRelationship
from sensiml.datamanager.metadata_value import MetadataValue
from sensiml.datamanager.segment import Segment
from sensiml.dclproj import DCLProject


def upload_project(client, name: str, dclproj_path: str):
    if name in client.list_projects()["Name"].values:
        print("Project with this name already exists.")
        return

    client.project = name
    basedir = os.path.dirname(dclproj_path)
    capture_dir = os.path.join(basedir, "data")
    dclproj = DCLProject(path=dclproj_path)

    # TODO: plugin config
    # plugin_config = dclproj.get("ProjectCapturePluginConfig", None)
    # if plugin_config is not None:
    #    client.project.plugin_config = plugin_config
    #    print("Capture Config Found, Updating...")
    #    client.project.update()

    session_set = []
    for _, session in dclproj.list_sessions().iterrows():
        if session["parameters"]:
            params = json.loads(session["parameters"])
            call = client.functions.create_function_call(params["name"])
            for k, v in params["inputs"].items():
                setattr(call, k, v)
        else:
            call = None

        new_segmenter = client.project.add_segmenter(
            session["name"],
            call,
            preprocess=session["preprocess"],
            custom=True if session["parameters"] else False,
        )
        session_set.append(new_segmenter)

    label_set = []
    for _, item in dclproj._list_table_raw("Label").iterrows():
        if item["metadata"] == 0:
            label = Label(client._connection, client.project)
            label.name = item["name"]
            label.is_dropdown = True if item["is_dropdown"] else False
            label.insert()
            label_set.append(label)
        else:
            metadata = Metadata(client._connection, client.project)
            metadata.name = item["name"]
            metadata.is_dropdown = True if item["is_dropdown"] else False
            metadata.insert()
            label_set.append(metadata)

    label_value_set = []
    for _, item in dclproj._list_table_raw("LabelValue").iterrows():
        if label_set[item["label"] - 1].metadata == False:
            label_value = LabelValue(
                client._connection, client.project, label_set[item["label"] - 1]
            )
            label_value.color = item["color"]
            label_value.value = item["value"]
            label_value.insert()
            label_value_set.append(label_value)
        else:
            metadata_value = MetadataValue(
                client._connection, client.project, label_set[item["label"] - 1]
            )
            metadata_value.color = None
            metadata_value.value = item["value"]
            metadata_value.insert()
            label_value_set.append(metadata_value)

    for _, capture in dclproj.list_captures().iterrows():
        print(
            "Uploading Capture data, metadata, and labels for {}".format(
                capture["name"]
            )
        )

        capture_obj = client.project.captures.create_capture(
            os.path.basename(capture["name"]),
            os.path.join(capture_dir, capture["name"]),
        )

        # TODO: Bulk metadata creation
        for _, metadata_relationship in dclproj.get_capture_metadata(
            capture["name"], include_ids=True
        ).iterrows():
            metadata_value = label_value_set[
                metadata_relationship["label_value_id"] - 1
            ]
            metadata = label_set[metadata_relationship["label_id"] - 1]
            metadata_relationship_obj = MetadataRelationship(
                client._connection,
                client.project,
                capture_obj,
                metadata,
                metadata_value,
            )
            metadata_relationship_obj.insert()

        # TODO: Bulk label creation
        for _, label_relationship in dclproj.list_capture_segments(
            capture["name"], include_ids=True
        ).iterrows():
            label_value = label_value_set[label_relationship["label_value_id"] - 1]
            label = label_set[label_relationship["label_id"] - 1]
            segmenter = session_set[label_relationship["segmenter_id"] - 1]["id"]
            label_relationship_obj = Segment(
                client._connection,
                client.project,
                capture_obj,
                segmenter,
                label,
                label_value,
            )
            label_relationship_obj.sample_start = label_relationship[
                "capture_sample_sequence_start"
            ]
            label_relationship_obj.sample_end = label_relationship[
                "capture_sample_sequence_end"
            ]
            label_relationship_obj.insert()
