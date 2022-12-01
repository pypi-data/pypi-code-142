class DefinitionException(Exception):
    pass


class ActorTypeIsNotDefined(DefinitionException):
    def __init__(self, repository: str):
        self.repository = repository
        super().__init__(f'Actor type must be defined in repository: {repository}')
