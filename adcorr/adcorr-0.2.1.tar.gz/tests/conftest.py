from pytest import Config, Function


def pytest_collection_modifyitems(items: list[Function], config: Config) -> None:
    """Adds the marker 'core' to all tests which do not have a marker.

    Args:
        items: A list of test functions.
        config: The pytest Config object.
    """
    for item in items:
        if not any(item.iter_markers()):
            item.add_marker("core")
