import os.path


def validate_file_exists(file_path):
    """
    Validates the file does exists. Throws an exception if it doesn't
    :param file_path: the file path
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Given input file {file_path} does not exists")


def validate_mandatory_args(mandatory_args):
    """
    Validates if all the arguments are specified for the processing. Throws an exception otherwise
    :param mandatory_args: list of argument values
    """
    if not all(mandatory_args):
        raise ValueError("Please provide all mandatory arguments. Read method doc or help text")
