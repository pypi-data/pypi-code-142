class SiteNameRequiredError(Exception):
    ...


class DuplicateSlugError(Exception):
    ...


class UnexpectedFormatError(Exception):
    ...


class OrphanFileError(Exception):
    ...


class MisplacedFileError(Exception):
    ...


class UnrecognizedStatusUpdateError(Exception):
    ...
