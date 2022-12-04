from typing import Dict, List, Mapping, Optional

from dependency_injector.containers import Container

from . import base, service


class Module(base.Module):
    def __init__(self, resources: Optional[Mapping[str, base.ResourceFactory]] = None,
                 services: Optional[Mapping[str, base.ServiceFactory]] = None,
                 modules: Optional[Mapping[str, base.ModuleFactory]] = None, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self._resources: Dict[str, base.Resource] = dict()
        self._services: Dict[str, service.Service] = dict()
        self._modules: Dict[str, Module] = dict()

        if resources:
            for name, provider in resources.items():
                instance = provider()
                if isinstance(instance, Container) and hasattr(instance, 'instance'):
                    instance = instance.instance()
                if isinstance(instance, base.Resource):
                    self._resources[name] = instance
        if services:
            for name, provider in services.items():
                instance = provider()
                if isinstance(instance, Container) and hasattr(instance, 'instance'):
                    instance = instance.instance()
                if isinstance(instance, base.Service):
                    self._services[name] = instance
        if modules:
            for name, provider in modules.items():
                instance = provider()
                if isinstance(instance, Container) and hasattr(instance, 'instance'):
                    instance = instance.instance()
                if isinstance(instance, base.Module):
                    self._modules[name] = instance

    @property
    def resources(self) -> List[base.Resource]:
        return list(self._resources.values())

    def get_resource(self, name) -> Optional[base.Resource]:
        return self._resources.get(name)

    @property
    def services(self) -> List[base.Service]:
        return list(self._services.values())

    def get_service(self, name) -> Optional[base.Service]:
        return self._services.get(name)

    @property
    def modules(self) -> List[base.Module]:
        return list(self._modules.values())

    def get_module(self, name) -> Optional[base.Module]:
        return self._modules.get(name)

    def sync_startup(self, application=None, *args, **kwargs):
        super().sync_startup(application=application, module=self, *args, **kwargs)

        for r in self.resources:
            r.sync_startup(application=application, module=self, *args, **kwargs)
        for m in self.modules:
            m.sync_startup(application=application, module=self, *args, **kwargs)
        for s in self.services:
            s.sync_startup(application=application, module=self, *args, **kwargs)

    def sync_shutdown(self, application=None, *args, **kwargs):
        for s in self.services:
            s.sync_shutdown(application=application, module=self, *args, **kwargs)
        for m in self.modules:
            m.sync_shutdown(application=application, module=self, *args, **kwargs)
        for r in self.resources:
            r.sync_shutdown(application=application, module=self, *args, **kwargs)

        super().sync_shutdown(application=application, module=self, *args, **kwargs)

    async def startup(self, application=None, *args, **kwargs):
        await super().startup(application=application, module=self, *args, **kwargs)

        for r in self.resources:
            await r.startup(application=application, module=self, *args, **kwargs)
        for m in self.modules:
            await m.startup(application=application, module=self, *args, **kwargs)
        for s in self.services:
            await s.startup(application=application, module=self, *args, **kwargs)

    async def shutdown(self, application=None, *args, **kwargs):
        for s in self.services:
            await s.shutdown(application=application, module=self, *args, **kwargs)
        for m in self.modules:
            await m.shutdown(application=application, module=self, *args, **kwargs)
        for r in self.resources:
            await r.shutdown(application=application, module=self, *args, **kwargs)

        await super().shutdown(application=application, module=self, *args, **kwargs)


class SessionModule(Module, base.SessionResource):
    def sync_session_begin(self, application=None, *args, **kwargs):
        super().sync_session_begin(application=application, module=self, *args, **kwargs)

        for r in self.resources:
            if not isinstance(r, base.SessionResource):
                continue
            r.sync_session_begin(application=application, module=self, *args, **kwargs)

        for m in self.modules:
            if not isinstance(m, base.SessionResource):
                continue
            m.sync_session_begin(application=application, module=self, *args, **kwargs)

        for r in self.services:
            if not isinstance(r, base.SessionResource):
                continue
            r.sync_session_begin(application=application, module=self, *args, **kwargs)

    def sync_session_finish(self, application=None, *args, **kwargs):
        for r in self.services:
            if not isinstance(r, base.SessionResource):
                continue
            r.sync_session_finish(application=application, module=self, *args, **kwargs)

        for m in self.modules:
            if not isinstance(m, base.SessionResource):
                continue
            m.sync_session_finish(application=application, module=self, *args, **kwargs)

        for r in self.resources:
            if not isinstance(r, base.SessionResource):
                continue
            r.sync_session_finish(application=application, module=self, *args, **kwargs)

        super().sync_session_finish(application=application, module=self, *args, **kwargs)

    async def session_begin(self, application=None, *args, **kwargs):
        await super().session_begin(application=application, module=self, *args, **kwargs)

        for r in self.resources:
            if not isinstance(r, base.SessionResource):
                continue
            await r.session_begin(application=application, module=self, *args, **kwargs)

        for m in self.modules:
            if not isinstance(m, base.SessionResource):
                continue
            await m.session_begin(application=application, module=self, *args, **kwargs)

        for r in self.services:
            if not isinstance(r, base.SessionResource):
                continue
            await r.session_begin(application=application, module=self, *args, **kwargs)

    async def session_finish(self, application=None, *args, **kwargs):
        for r in self.services:
            if not isinstance(r, base.SessionResource):
                continue
            await r.session_finish(application=application, module=self, *args, **kwargs)

        for m in self.modules:
            if not isinstance(m, base.SessionResource):
                continue
            await m.session_finish(application=application, module=self, *args, **kwargs)

        for r in self.resources:
            if not isinstance(r, base.SessionResource):
                continue
            await r.session_finish(application=application, module=self, *args, **kwargs)

        await super().session_finish(application=application, module=self, *args, **kwargs)
