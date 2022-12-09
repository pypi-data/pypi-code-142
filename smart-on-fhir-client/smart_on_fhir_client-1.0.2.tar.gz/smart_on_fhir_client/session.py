from aiohttp import ClientSession

# here we defined a global session object as a singleton object
# to be able to reuse it among all requests for performance reasons


# noinspection PyPep8Naming
class SessionManager:
    def __init__(self):
        self._session = None

    @property
    def fhir_client_session(self) -> ClientSession:
        """

        Returns:

        """
        assert self._session is not None, "session manager has not been instanced"
        return self._session

    async def close(self):
        """ """
        await self._session.close()

    async def init(self):
        if self._session is None:
            self._session = ClientSession()
        else:
            raise ValueError("Client Session already created")

    async def __aenter__(self):
        """

        Returns:

        """
        await self.init()
        return await self._session.__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """

        Args:
            exc_type:
            exc_val:
            exc_tb:
        """
        await self._session.__aexit__(exc_type, exc_val, exc_tb)


session_manager = SessionManager()
