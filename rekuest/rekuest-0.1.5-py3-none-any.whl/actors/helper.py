from pydantic import BaseModel
from rekuest.actors.base import Actor
from rekuest.api.schema import LogLevelInput
from rekuest.messages import Assignation, Provision
from koil import unkoil


class AssignationHelper(BaseModel):
    assignation: Assignation

    async def alog(self, level: LogLevelInput, message: str) -> None:
        raise NotImplementedError()

    async def aprogress(self, progress: int) -> None:
        raise NotImplementedError()

    @property
    def user(self) -> str:
        return self.assignation.user

    class Config:
        arbitrary_types_allowed = True


class ProvisionHelper(BaseModel):
    provision: Provision

    async def alog(self, level: LogLevelInput, message: str) -> None:
        raise NotImplementedError()

    @property
    def guardian(self) -> str:
        return self.provision.guardian


class ThreadedAssignationHelper(AssignationHelper):
    def progress(self, progress: int) -> None:
        unkoil(self.aprogress, progress=progress)


class AsyncAssignationHelper(AssignationHelper):
    async def alog(self, message: str, level: LogLevelInput = LogLevelInput.DEBUG):

        await self.actor.transport.log_to_assignation(
            id=self.assignation.assignation, level=level, message=message
        )


class AsyncProvisionHelper(ProvisionHelper):
    async def alog(self, message: str, level: LogLevelInput = LogLevelInput.DEBUG):
        await self.actor.transport.log_to_provision(
            id=self.actor.provision.id, level=level, message=message
        )
