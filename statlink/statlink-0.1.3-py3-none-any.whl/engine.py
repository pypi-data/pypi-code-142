from __future__ import annotations

import asyncio
import subprocess
from abc import abstractmethod
from contextlib import AbstractAsyncContextManager
from functools import partial
from typing import Dict, Optional, Type

import aiohttp
from playwright import async_api as playwright
from playwright._impl._driver import compute_driver_executable, get_driver_env

from .request import Request, RequestConnectionError, RequestError, RequestTimeoutError
from .response import Response


class Engine(AbstractAsyncContextManager):  # type: ignore
    @abstractmethod
    async def fetch(self, request: "Request") -> Optional[Response]:
        pass  # pragma: no cover


class AioHTTPEngine(Engine):
    def __init__(self):
        conn = aiohttp.TCPConnector(limit_per_host=20, limit=30)
        self.client_session = aiohttp.ClientSession(connector=conn)

    async def __aenter__(self) -> AioHTTPEngine:
        await self.client_session.__aenter__()
        return self

    async def __aexit__(self, *exc):
        await self.client_session.__aexit__(*exc)

    async def fetch(self, request: "Request") -> Optional[Response]:
        try:
            async with self.client_session.get(
                request.url, timeout=request.timeout
            ) as client_response:
                response = Response(
                    status=client_response.status,
                    content_type=client_response.headers.get("Content-Type"),
                )
                if response.is_html():
                    try:
                        response.text = await client_response.text()
                    except ValueError:
                        pass
                if not response.text:
                    client_response.close()
                return response
        except asyncio.TimeoutError:
            raise RequestTimeoutError()
        except aiohttp.ClientConnectionError as exc:
            raise RequestConnectionError(exc)
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            raise RequestError(exc)


class BrowserEngine(Engine):
    def __init__(self, browser_type: str):
        self.playwright_context = playwright.async_playwright()
        self.browser_type = browser_type
        self.browser: playwright.Browser

    async def __aenter__(self) -> BrowserEngine:
        async_playwright = await self.playwright_context.__aenter__()
        try:
            self.browser = await self.launch_browser(async_playwright)
        except playwright.Error as exc:
            if "Executable doesn't exist" in str(exc):
                install_browser_executable(self.browser_type)
                self.browser = await self.launch_browser(async_playwright)
            else:
                raise
        return self

    async def __aexit__(self, *exc):
        await self.playwright_context.__aexit__(*exc)

    async def launch_browser(
        self, async_playwright: playwright.Playwright
    ) -> playwright.Browser:
        browser: playwright.Browser = await getattr(
            async_playwright, self.browser_type
        ).launch()
        return browser

    async def fetch(self, request: "Request") -> Optional[Response]:
        page = await self.browser.new_page()
        try:
            response = await page.goto(
                request.url,
                timeout=request.timeout * 1000,
                wait_until="domcontentloaded",
            )

            if response:
                return Response(
                    text=await page.content(),
                    status=response.status,
                    content_type=response.headers.get("Content-Type"),
                )

        except playwright.TimeoutError:
            raise RequestTimeoutError()

        except playwright.Error as exc:
            error_message = str(exc).lower()
            connection_error_messages = [
                "err_name_not_resolved",
                "err_address_unreachable",
            ]
            if any(message in error_message for message in connection_error_messages):
                raise RequestConnectionError()
            raise RequestError(self._truncate_error(str(exc)))

        except asyncio.CancelledError:
            raise

        except Exception as exc:
            raise RequestError(exc)

        finally:
            await page.close()

    @staticmethod
    def _truncate_error(error_message: str) -> str:
        return error_message.split("\n=", maxsplit=1)[0].capitalize()


ENGINE_MAPPING: Dict[str, Type[Engine]] = {
    "aiohttp": AioHTTPEngine,
    **{
        browser_type: partial(BrowserEngine, browser_type=browser_type)  # type: ignore
        for browser_type in ["chromium", "firefox", "webkit"]
    },
}


def install_browser_executable(browser_type: str) -> None:
    driver_executable = compute_driver_executable()
    subprocess.run(
        [str(driver_executable), "install", browser_type], env=get_driver_env()
    )
