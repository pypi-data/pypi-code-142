import os
import copy
import pathlib
from polly.errors import paramException

import polly.constants as const


def parameter_check_for_repo_id(repo_id):
    """Checking for validity of repo id
    Args:
        repo_id (): Repository Id of omixatlas

    Raises:
        paramException: Error if repo id is empty or is not str or int
    """
    if not repo_id:
        raise paramException(
            title="Param Error",
            detail="repo_id should not be empty",
        )
    elif type(repo_id) != str and type(repo_id) != int:
        raise paramException(
            title="Param Error",
            detail="repo_id should be str or int",
        )


# TODO: See if this can be merged with data_metadata_parameter_check
# Difference between both the functions is in One `data` and `metadata` keys optional
# In other both `data` and `metadata` keys are mandatory
def check_source_folder_path_for_ingestion(source_folder_path: any):
    """
    checks if source folder path is a dict and if yes then checks
    the folders inside the source folder path
    At least one of the data or metada folder paths must be present

    Arguments:
        source_folder_path -- dict with optional metadata and data keys
        and folder paths as values
    """
    if source_folder_path and isinstance(source_folder_path, dict):
        for key in source_folder_path.keys():
            if key not in const.INGESTION_FILES_PATH_DIR_NAMES:
                raise paramException(
                    title="Param Error",
                    detail="source_folder_path should be a dict with valid data and"
                    + f"metadata path values in the format {const.FILES_PATH_FORMAT} ",
                )
            else:
                data_directory = os.fsencode(source_folder_path[key])
                if not os.path.exists(data_directory):
                    raise paramException(
                        title="Param Error",
                        detail="`key` path passed is not found. "
                        + "Please pass the correct path and call the function again",
                    )
    else:
        raise paramException(
            title="Param Error",
            detail="source_folder_path should be a dict with valid data and"
            + f" metadata path values in the format {const.FILES_PATH_FORMAT} ",
        )


def data_metadata_parameter_check(source_folder_path: dict):
    """
    Sanity check for data and metadata path parameters
    """
    if not (source_folder_path and (isinstance(source_folder_path, dict))):
        raise paramException(
            title="Param Error",
            detail="source_folder_path should be a dict with valid data and"
            + f" metadata path values in the format {const.FILES_PATH_FORMAT} ",
        )

    if "data" not in source_folder_path:
        raise paramException(
            title="Param Error",
            detail=f"{source_folder_path} does not have `data` path."
            + f" Format the source_folder_path_dict like this  {const.FILES_PATH_FORMAT}",
        )

    if "data" in source_folder_path:
        data_directory = os.fsencode(source_folder_path["data"])
        if not os.path.exists(data_directory):
            raise paramException(
                title="Param Error",
                detail="`data` path passed is not found. "
                + "Please pass the correct path and call the function again",
            )

    if "metadata" not in source_folder_path:
        raise paramException(
            title="Param Error",
            detail=f"{source_folder_path} does not have `metadata` path. "
            + "Format the source_folder_path_dict like this  {const.FILES_PATH_FORMAT}",
        )

    if "metadata" in source_folder_path:
        data_directory = os.fsencode(source_folder_path["metadata"])
        if not os.path.exists(data_directory):
            raise paramException(
                title="Param Error",
                detail="`metadata` path passed is not found. Please pass the correct path and call the function again",
            )


def check_for_single_word_multi_word_extension(
    data_directory: list, data_file_format_constants: list
):
    """iterate the data directory and check for different types of extensions
    in data files

    Args:
        data_directory (list): dataset files directory
        data_file_format_constants (list): List of approved formats
    """
    for file in os.listdir(data_directory):
        file = file.decode("utf-8")
        # skip hidden files
        if not file.startswith("."):
            file_ext = pathlib.Path(file).suffixes
            if len(file_ext) == 0:
                # file without extension
                raise paramException(
                    title="Param Error",
                    detail=f"File format for file {file} is not available"
                    + f"It can be => {data_file_format_constants}",
                )
            elif len(file_ext) == 1:
                # file with single word extension
                file_ext_single_word = file_ext[-1]
                if file_ext_single_word not in data_file_format_constants:
                    raise paramException(
                        title="Param Error",
                        detail=f"File format for file {file} is invalid."
                        + f"It can be => {data_file_format_constants}",
                    )
            elif len(file_ext) > 1:
                # file with multi word extension
                # or `.`'s present in file name

                # check for multiword extensions
                compression_type_check = file_ext[-1]

                # compression types
                compression_types = copy.deepcopy(const.COMPRESSION_TYPES)
                # concatenating 2nd last and last word together to check
                # for multiword extension
                # pathlib.Path('my/library.tar.gar').suffixes
                # ['.tar', '.gz']
                file_type_multi_word = file_ext[-2] + file_ext[-1]
                if (compression_type_check in compression_types) and (
                    file_type_multi_word in data_file_format_constants
                ):
                    # multi word extension
                    continue
                elif file_ext[-1] in data_file_format_constants:
                    # single word extension with `.`'s in file which is accepted
                    continue
                elif file_ext[-1] not in data_file_format_constants:
                    raise paramException(
                        title="Param Error",
                        detail=f"File format for file {file} is invalid."
                        + f"It can be => {data_file_format_constants}",
                    )


def get_file_format_constants() -> dict:
    """
    Returns file format info from public assests url
    """
    response = copy.deepcopy(const.FILE_FORMAT_CONSTANTS)
    return response


def data_metadata_file_ext_check(source_folder_path: dict):
    """
    Check extension for data and metadata file names
    """
    format_constants = get_file_format_constants()
    data_file_format_constants = format_constants.get("data")
    # data_source_folder_path = source_folder_path["data"]
    data_source_folder_path = source_folder_path.get("data", "")

    if data_source_folder_path:
        data_directory = os.fsencode(data_source_folder_path)

        try:
            check_for_single_word_multi_word_extension(
                data_directory, data_file_format_constants
            )
        except Exception as err:
            raise err

    metadata_file_format_constants = format_constants["metadata"]
    # metadata_source_folder_path = source_folder_path["metadata"]
    metadata_source_folder_path = source_folder_path.get("metadata", "")
    metadata_directory = os.fsencode(metadata_source_folder_path)
    if metadata_source_folder_path:
        for file in os.listdir(metadata_directory):
            file = file.decode("utf-8")
            # skip hidden files
            if not file.startswith("."):
                file_ext = pathlib.Path(file).suffixes
                file_ext_single_word = file_ext[-1]
                if file_ext_single_word not in metadata_file_format_constants:
                    raise paramException(
                        title="Param Error",
                        detail=f"File format for file {file} is invalid."
                        + f"It can be => {metadata_file_format_constants}",
                    )


def check_data_metadata_file_path(source_folder_path: dict):
    """
    Check Metadata and Data files folders to test for empty case.
    in case of update, data/metadata folders are optional.
    Only if present in the source_folder_path dict and is a directory, empty case checked.
    """
    data_source_folder_path = source_folder_path.get("data", "")
    metadata_source_folder_path = source_folder_path.get("metadata", "")

    if data_source_folder_path and os.path.isdir(data_source_folder_path):
        if not os.listdir(data_source_folder_path):
            raise paramException(
                title="Param Error",
                detail=f"{data_source_folder_path} does not contain any datafiles. "
                + "Please add the relevant data files and try again",
            )

    if metadata_source_folder_path and os.path.isdir(metadata_source_folder_path):
        if not os.listdir(metadata_source_folder_path):
            raise paramException(
                title="Param Error",
                detail=f"{metadata_source_folder_path} does not contain any metadatafiles. "
                + "Please add the relevant metadata files and try again",
            )


def create_file_name_with_extension_list(file_names: list, file_ext_req=True) -> list:
    """Decode the file name in bytes to str

    Args:
        data_file_names (list): data file name in bytes
    Returns:
        list: data file names in str
    """
    file_names_str = []
    # convert file names from bytes to strings
    # file name is kept with extension here
    for file in file_names:
        file = file.decode("utf-8")
        if not file.startswith("."):
            if not file_ext_req:
                file = pathlib.Path(file).stem
            file_names_str.append(file)
    return file_names_str


def data_metadata_file_dict(
    metadata_file_names_str: list, data_file_names_str: list
) -> list:
    """Construct data metadata file name dict and also return list of files which are unmapped
    Convention Followed in naming -> Metadata and Data File Name -> Will always be same
    Extension will be different -> Name always same

    Args:
        metadata_file_names_str (list): List of all metadata file names
        data_file_names_str (list): list of all data file names with extensions

    Returns:
        list: Returns list of mapped and unmapped files
    """
    # metadata file name -> key, data file name with extension -> value
    data_metadata_mapping_dict = {}

    # file_format = get_file_format_constants()
    # file_format_data = file_format.get("data", [])

    unmapped_file_names = []
    for data_file in data_file_names_str:
        data_file_name = get_file_name_without_suffixes(data_file)

        # check for matching data and metadata file name
        # convention for the system to know data and metadata mapping
        # also removing the metadata file from the list
        # which maps to data file
        # so as to return the unmapped metadata files at last if any
        if data_file_name in metadata_file_names_str:
            data_metadata_mapping_dict[data_file_name] = data_file
            metadata_file_names_str.remove(data_file_name)
        else:
            unmapped_file_names.append(data_file_name)
    return data_metadata_mapping_dict, unmapped_file_names, metadata_file_names_str


def data_metadata_file_mapping_conditions(
    unmapped_data_file_names: list,
    unmapped_metadata_file_names: list,
    data_metadata_mapping_dict: dict,
) -> dict:
    """Different conditions to check for data metadata mapping

    Args:
        unmapped_file_names (list): data file names which are not mapped
        metadata_file_names_str (list): metadata file names list
        data_metadata_mapping_dict (dict): dict of data metadata mapping

    Returns:
        dict: data_metadata mapping dict if conditions succeed
    """
    # data and metadata file names are unmapped
    if len(unmapped_data_file_names) > 0 and len(unmapped_metadata_file_names) > 0:
        raise paramException(
            title="Missing files",
            detail=f" No metadata for these data files {unmapped_data_file_names}. "
            + f"No data for these metadata files {unmapped_metadata_file_names}. "
            + "Please add the relevant files or remove them.",
        )
    elif len(unmapped_data_file_names) > 0:
        raise paramException(
            title="Missing files",
            detail=f" No metadata for these data files {unmapped_data_file_names}"
            + ". Please add the relevant files or remove them.",
        )
    elif len(unmapped_metadata_file_names) > 0:
        raise paramException(
            title="Missing files",
            detail=f"No data for these metadata files {unmapped_metadata_file_names}"
            + ". Please add the relevant files or remove them.",
        )
    else:
        return data_metadata_mapping_dict


def get_file_name_without_suffixes(data_file: str) -> str:
    """
    Returns just the file name without the suffixes.
    This functionality is written according to the rules of data file naming
    i) Data Files can have single extension
    ii) Data Files can have multiple extension
        => Multiword Extensions only possible if
        => Data file name has one main extension and one compressed extension
        => Examples are -> `.gct.bz`, `.h5ad.zip`
    iii) Data Files can have `.`'s in the names
    """
    file_format = get_file_format_constants()
    file_format_data = file_format.get("data", [])
    file_ext = pathlib.Path(data_file).suffixes
    if len(file_ext) == 1:
        # single word extension
        data_file_name = pathlib.Path(data_file).stem
    elif len(file_ext) > 1:
        # Either file with multi word extension
        # or `.`'s present in file name
        # check for multiword extensions
        compression_type_check = file_ext[-1]

        # compression types
        compression_types = copy.deepcopy(const.COMPRESSION_TYPES)
        # concatenating 2nd last and last word together to check
        # for multiword extension
        # pathlib.Path('my/library.tar.gz').suffixes
        # ['.tar', '.gz']

        if compression_type_check in compression_types:
            # multi word extension case
            # data_file -> file name with extension and compression format
            # file name with extension attached with `.`
            file_name_with_extension = pathlib.Path(data_file).stem

            # check if file_name_with_extension has an extension or is it a name
            # for ex
            # Case 1 => abc.gct.bz => after compression ext split
            # abc.gct => .gct => valid supported extension
            # Case 2 => abc.tar.gz => after compression ext split
            # abc.tar => .tar => valid compression type
            # Case 3 => abc.bcd.gz => Only zip as extension, no other extension

            file_main_ext = pathlib.Path(file_name_with_extension).suffix
            if file_main_ext in file_format_data:
                # file name
                data_file_name = pathlib.Path(file_name_with_extension).stem
            elif file_main_ext in compression_types:
                # second compression type
                data_file_name = pathlib.Path(file_name_with_extension).stem
            else:
                data_file_name = file_name_with_extension
        else:
            # single word extension with `.`'s in file which is accepted
            data_file_name = pathlib.Path(data_file).stem
    return data_file_name


def parameter_check_for_priority(priority: str):
    if not isinstance(priority, str):
        raise paramException(
            title="Param Error",
            detail="`priority` should be a string. Only 3 values are allowed i.e. `low`, `medium`, `high`",
        )

    if priority not in ["low", "medium", "high"]:
        raise paramException(
            title="Param Error",
            detail="`priority` varaible can have these 3 values => `low`, `medium`, `high` ",
        )


def check_create_omixatlas_parameters(
    display_name: str,
    description: str,
    repo_name: str,
    image_url: str,
    components: list,
    category: str,
):
    """Sanity check for Parameters passed in Create Method

    Args:
        display_name (str): Display name of the Omixatlas
        description (str): Description of the Omixatlas
        repo_name (str): proposed repo name for the omixatlas
        image_url (str): image url provided for the icon for the omixatlas
        components (list): components to be added in the omixatlas
        category (str): category definition of the omixatlas
    """
    str_params = [display_name, description, repo_name, image_url]
    for param in str_params:
        if not isinstance(param, str):
            raise paramException(
                title="Param Error", detail=f"{param} should be a string"
            )

    if not isinstance(components, list):
        raise paramException(
            title="Param Error", detail=f"{components} should be a list"
        )

    if not isinstance(category, str) or (category not in const.OMIXATLAS_CATEGORY_VALS):
        raise paramException(
            title="Param Error",
            detail=f"{category} should be a string and its value must be one of {const.OMIXATLAS_CATEGORY_VALS}",
        )
