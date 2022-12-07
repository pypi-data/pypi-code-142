from pyguarantees import severity


def _parse_what_dict(what_dict: dict, tabs: str = "\t") -> str:
    err_str = ""
    for key, val in what_dict.items():
        if type(val) is dict:
            err_str += f"{tabs}key: \n"
            err_str += _parse_what_dict(val, tabs + "\t")
        else:
            err_str += f"{tabs}{str(key)}: {str(val)} \n"

    return err_str


def construct_err_str(
        qualname: str,
        module: str,
        guarantee_name: str,
        parameter_name: str,
        error_severity: int,
        what_dict: dict = None
) -> str:
    severity_str_dict = {
        severity.DEBUG: "DEBUG",
        severity.INFO: "INFO",
        severity.WARN: "WARN",
        severity.ERROR: "ERROR",
        severity.FATAL: "FATAL"
    }
    err_str = f"\n\tWhere: \n"
    err_str += f"\t\tModule: {module} \n"
    err_str += f"\t\tName: {qualname} \n"
    err_str += f"\tSeverity: {severity_str_dict[error_severity]} \n"
    err_str += f"\tGuarantee: {guarantee_name} \n"
    err_str += f"\tParameter: {parameter_name} \n"
    err_str += _parse_what_dict(what_dict)
    return err_str
