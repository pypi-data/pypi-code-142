from typing import Callable
from rekuest.actors.base import Actor
from rekuest.agents.transport.base import AgentTransport
from rekuest.api.schema import TemplateFragment
from rekuest.messages import Provision


ActorBuilder = Callable[[Provision, AgentTransport, TemplateFragment], Actor]
