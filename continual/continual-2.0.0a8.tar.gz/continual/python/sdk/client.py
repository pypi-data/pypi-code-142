from __future__ import annotations
import grpc
from typing import Optional
from google.protobuf.empty_pb2 import Empty
from continual.python.sdk.config import Config
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import management_pb2_grpc
from continual.python.sdk.projects import ProjectManager, Project
from continual.python.sdk.organizations import OrganizationManager
from continual.python.sdk.runs import RunManager
from continual.python.sdk.users import UserManager, User
from continual.python.sdk.interceptors import AuthInterceptor
from continual.python.sdk.exceptions import normalize_exceptions_for_class
from continual.python.utils.client_utils import get_management_channel
from importlib.metadata import version

try:
    __version__ = version("continual")
except:
    __version__ = "local-dev"
from continual.python.sdk.identifiers import ProjectEnvironmentIdentifer


class Client:
    """Continual client."""

    users: UserManager
    """User manager."""

    projects: ProjectManager
    """Project manager."""

    organizations: OrganizationManager
    """Organization manager."""

    runs: RunManager
    """Runs manager"""

    config: Config
    """Client configuration."""

    _management: management_pb2_grpc.ManagementAPIStub
    """Management GRPC API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        endpoint: Optional[str] = None,
        project: Optional[str] = None,
        environment: Optional[str] = None,
        verify: bool = True,
    ):
        """Initialize client.

        It is recommended to use `continual login` to generate a
        local on-disk API key.

        Arguments:
            api_key: API key.
            project: Default project.
            endpoint: Cluster endpoint (Private Cloud only)
            environment: Project environment
            verify: Whether or not to verify the arguments on init
        """

        # Initialize config to process args
        self.config = Config(
            endpoint=endpoint, api_key=api_key, project=project, environment=environment
        )

        if self.config.api_key and verify:
            self.set_config_api_key(api_key=self.config.api_key, save=False)
        else:
            # At the very least initialie the management channel to allow register and login
            self._init_grpc_connnections(api_key=self.config.api_key)
            self._init_managers()

        # Initialize managers that only depend on client
        self.users = UserManager(client=self)
        self.organizations = OrganizationManager(client=self)
        self.projects = ProjectManager(client=self)

        # Verify and set proj and env IF they are set in config
        if self.config.project and verify:
            self.set_config_project(project=self.config.project, save=False)
            self.set_config_environment(environment=self.config.environment, save=False)

    def _init_managers(self):
        # Initialize managers.
        parent = self.config.project
        if parent is None:
            parent = "projects/-"
        else:
            env = self.config.environment
            if (
                env == None
                or env == "master"
                or env == "main"
                or env == "production"
                or len(env) == 0
            ):
                env = "prod"
            if env != "prod":
                parent = f"{self.config.project}@{self.config.environment}"

        self.runs = RunManager(client=self, parent=parent)

    def _init_grpc_connnections(self, api_key):
        """Init auth"""
        auth_interceptor = AuthInterceptor(lambda: api_key)
        self._mgmt_channel = get_management_channel(self.config.endpoint)

        self._mgmt_channel = grpc.intercept_channel(
            self._mgmt_channel, auth_interceptor
        )
        self._management = normalize_exceptions_for_class(
            management_pb2_grpc.ManagementAPIStub(self._mgmt_channel)
        )

    def _verify_api_key(self):
        """Verifies that the API key is valid by calling CheckViewer"""
        try:
            self.check_viewer()
        except Exception as e:
            api_key = self._mgmt_channel._interceptor.api_key_getter()
            raise Exception(f"Unable to verify API key {api_key}. {str(e)}")

    def set_config_api_key(self, api_key: str, save=False) -> str:
        """Sets config API key and reinitialize the managers for this client"""
        # Reinitalize Initialize GRPC connections.
        self._init_grpc_connnections(api_key=api_key)

        self._verify_api_key()
        # if api key is an api key and not a session, set project
        if api_key.startswith("apikey/"):
            api_key_project = self.get_api_key_project(api_key=api_key)
            self.config.set_project(project=api_key_project.name, save=save)

        self.config.set_api_key(api_key=api_key, save=save)

        # Reset managers
        self._init_managers()

    def _verify_project(self, project: str) -> str:
        # Verify project name and return fqn
        try:
            for p in self.projects.list_all():
                if project == p.name or project.split("/")[-1] in {
                    p.id,
                    p.display_name,
                }:
                    return p.name

            raise Exception(
                f"Project '{project}' not found. Make sure to provide fully qualified project name or unique project ID."
            )
        except Exception as e:
            raise Exception(f"Unable to verify project '{project}'. {str(e)}")

    def set_config_project(self, project: str, save=False) -> str:
        """Sets config project and reinitialize the managers for this client"""
        # Here ensure that if the API key is blank, you cannot set a project (you need to login first)
        if not self.config.api_key and project:
            raise Exception(
                f"API key is empty. Cannot set project '{project}' until client has valid API key."
            )

        project_name = self._verify_project(project=project)
        self.config.set_project(project=project_name, save=save)

        # Reset managers
        self._init_managers()

    def _verify_environment(self, project: str, environment: str):
        # Verify environment name after project is verified
        try:
            proj = self.projects.get(project)

            env_identifier_to_verify = ProjectEnvironmentIdentifer(
                project_name_or_id=project, environment_name_or_id=environment
            )

            environment_names = [
                ProjectEnvironmentIdentifer(project_name_or_id=e.name).environment_name
                for e in proj.environments.list_all()
            ]
            if (
                env_identifier_to_verify.environment_name not in environment_names
                and not env_identifier_to_verify.environment_is_default
            ):
                raise Exception(f"Environment '{environment}' not found.")

        except Exception as e:
            raise Exception(f"Unable to verify environment '{environment}'. {str(e)}")

    def set_config_environment(self, environment: str, save=False) -> str:
        """Sets config env and reinitialize the managers for this client"""
        self._verify_environment(project=self.config.project, environment=environment)
        self.config.set_environment(environment=environment, save=save)

        # Reset managers
        self._init_managers()

    def __del__(self) -> None:
        """Clean up active gRPC channels and threads when client deleted."""
        if hasattr(self, "_mgmt_channel"):
            self._mgmt_channel.close()
        if hasattr(self, "_fs_channel"):
            self._fs_channel.close()
        if hasattr(self, "_gw_channel"):
            self._gw_channel.close()

    def viewer(self) -> User:
        """Currently authenticated user."""
        resp = self._management.GetViewer(Empty())
        return User.from_proto(resp, client=self)

    def check_viewer(self) -> User:
        """Verify if Currently authenticated user."""
        self._management.CheckViewer(Empty())

    def get_api_key_project(self, api_key: str) -> Project:
        req = management_pb2.GetApiKeyProjectRequest(name=api_key)
        resp = self._management.GetApiKeyProject(req)
        return Project.from_proto(resp, client=self)

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        save: bool = True,
    ) -> User:
        """Register a new account.

        This function registers and authenticates a new user.  This is
        meant only for automation purposes.  Please sign up directly on
        https://continual.ai instead.

        Arguments:
            first_name: First name of user.
            last_name: Last name of user
            email: Email address.
            password: Password.
            save: Whether to persist API key to config file

        Returns:
            The newly created authenticated user.
        """
        req = management_pb2.RegisterRequest(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
        resp = self._management.Register(req)

        # No need to reverify API key in response
        self.config.set_api_key(resp.auth_token, save=save)
        self._init_grpc_connnections(self.config.api_key)
        self.config.email = email
        return User.from_proto(resp.user, client=self)

    def login(self, email: str, password: str, save: bool = True) -> User:
        """Login to Continual.

        It is strongly recommended to use `continual login` CLI
        or an API key instead of logging in via the SDK.

        Args:
            email: Email address.
            password: Password.
            save: Whether to persist API key to config file
        Returns:
            The authenticated user.
        """
        req = management_pb2.LoginRequest(email=email, password=password)
        resp = self._management.Login(req)

        # No need to reverify API key in response
        self.config.set_api_key(resp.auth_token, save=save)
        self._init_grpc_connnections(self.config.api_key)
        self.config.email = email
        return User.from_proto(resp.user, client=self)

    def logout(self) -> None:
        """Logout.

        Logs out current session deleting the associated API key.
        """
        if self.config.api_key is not None and self.config.api_key != "":
            self._management.Logout(Empty())
            self.config.set_api_key(api_key=None)
            self.config.email = None
            self.config.save()

    def version(self):
        client_version = __version__
        req = management_pb2.GetServerVersionRequest(client_version=client_version)
        resp = self._management.GetServerVersion(req)
        return client_version, resp.server_version, resp.upgrade_required
