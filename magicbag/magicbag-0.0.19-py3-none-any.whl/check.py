"""String check util."""


def prefix_check(source, prefix):
    """Check string start with.

    Args:
        source (str): source string
        prefix (tuple): prefix tuple list

    Returns:
        (bool, str): True/False; matched prefix string or None;
    """
    if not isinstance(source, str):
        return False

    if not isinstance(prefix, tuple):
        return False

    for content in prefix:
        if source[: len(content)] == content:
            # match prefix
            return True, content

    # not match
    return False, None
