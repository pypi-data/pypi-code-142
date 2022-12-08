def get_git_parameters(branch: str, key_file: str, single_branch: bool, depth: int = 0) -> dict:
    """ Obtain the extra git parameters.
    :param branch: The branch to use, if it is not given, the master or main branch is used.
    :param key_file: The file with the key.
    :param single_branch: Whether to clone a single branch or all the repository.
           By default, only the specified branch, it is faster.
    :param depth: Create a shallow clone of that depth. By default, 0.
    :return: A dict with the extra git parameters.
    """
    kwargs: dict = {'branch': branch} if branch else {}
    if single_branch:
        kwargs['single-branch'] = single_branch
    if depth > 0:
        kwargs['depth'] = depth
    if key_file:
        kwargs['env'] = {'GIT_SSH_COMMAND': f'ssh -i {key_file} -o StrictHostKeyChecking=no'}
    return kwargs
