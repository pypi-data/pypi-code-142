from typing import Optional

from pydantic import Field

from rekuest.postmans.vars import current_postman
from koil.composition import KoiledModel


class BasePostman(KoiledModel):
    """Postman


    Postmans are the schedulers of the arkitekt platform, they are taking care
    of the communication between your app and the arkitekt-server. And
    provide abstractions to map the asynchornous message-based nature of the arkitekt-server to
    the (a)sync nature of your app. It maps assignations to functions or generators
    depending on the definition, to mimic an actor-like behaviour.

    """

    async def __aenter__(self):
        current_postman.set(self)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        current_postman.set(None)
