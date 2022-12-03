class ProjectRepositoryError(Exception):
    ...


class ProjectEmpty(ProjectRepositoryError):
    ...


class ProjectExist(ProjectRepositoryError):
    ...


class ProjectNotFound(ProjectRepositoryError):
    ...


class InvalidCSVPath(ProjectRepositoryError):
    ...