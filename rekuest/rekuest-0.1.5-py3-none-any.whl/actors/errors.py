from rekuest.errors import RekuestError


class ActorException(RekuestError):
    pass


class UnknownMessageError(ActorException):
    pass


class ThreadedActorCancelled(ActorException):
    pass
