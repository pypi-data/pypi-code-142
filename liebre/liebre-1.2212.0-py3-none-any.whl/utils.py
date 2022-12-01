import json


def get_partition_queue_name(queue_name, partition):
    return f'{queue_name}.{partition}'


def serialize_content(content):
    return json.dumps(
        content,
        ensure_ascii=False,
        separators=(',',
                    ':'),
    )


def deserialize_content(content):
    if content is None:
        return

    try:
        deserialized_content = json.loads(content)
        if isinstance(content, str):
            deserialized_content = json.loads(deserialized_content)
    except json.JSONDecodeError:
        deserialized_content = content

    return deserialized_content


def get_suffixed_queue_name(queue, suffix):
    return f'{queue}.{suffix}'
