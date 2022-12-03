import logging

from .settings import (
    BIND_PASSWORD,
    BIND_USER,
    BIND_END_POINT,
    REDIS_CONNECTION,
    BANK_ID,
    VIEW_ID,
)
from .services.bind_service import BindService
from .services.cache_service import CacheService
from .requests_payload.transfer_payload import TransferPayload
from .requests_payload.debin_payload import DebinPayload

logger = logging.getLogger(__name__)


class Sdk:
    def login(self, refresh=False) -> str:
        cs = CacheService()
        if REDIS_CONNECTION:
            if not cs.get_credentials() or refresh:
                rta = BindService.login(BIND_USER, BIND_PASSWORD, BIND_END_POINT)
                cs.set_credentials(rta.get("token"), rta.get("expires_in") - 100)
            return cs.get_credentials()
        else:
            return BindService.login(BIND_USER, BIND_PASSWORD, BIND_END_POINT).get(
                "token"
            )

    def is_bancked(self, cuit: int) -> dict:
        return BindService.bancked_cuit(cuit, str(self.login()), BIND_END_POINT)

    def get_views(self) -> dict:
        return BindService.get_views(str(self.login()), BIND_END_POINT, BANK_ID)

    def get_accounts(self) -> dict:
        return BindService.get_accounts(
            str(self.login()), BIND_END_POINT, BANK_ID, VIEW_ID
        )

    def get_account(self, account_id: str) -> dict:
        return BindService.get_account(
            account_id, str(self.login()), BIND_END_POINT, BANK_ID, VIEW_ID
        )

    def get_account_movements(self, account_id: str, query=None) -> dict:
        return BindService.get_account_movements(
            account_id, str(self.login()), BIND_END_POINT, BANK_ID, VIEW_ID
        )

    def get_account_details_by_alias(self, alias: str) -> dict:
        return BindService.get_account_by_alias(
            alias, str(self.login()), BIND_END_POINT
        )

    def get_account_details_by_cbu_cvu(self, cbu_cvu: int) -> dict:
        return BindService.get_account_by_cbu_cvu(
            cbu_cvu, str(self.login()), BIND_END_POINT
        )

    def send_transfer(self, payload: TransferPayload, account_sender_id: str):
        return BindService.send_transfer(
            payload.to_json(),
            account_sender_id,
            str(self.login()),
            BIND_END_POINT,
            BANK_ID,
            VIEW_ID,
        )

    def get_transfers(self, account_id: str) -> dict:
        return BindService.get_transfers(
            account_id,
            str(self.login()),
            BIND_END_POINT,
            BANK_ID,
            VIEW_ID,
        )

    def get_transfer(self, transfer_id: str, account_id: str) -> dict:
        return BindService.get_transfer(
            transfer_id,
            account_id,
            str(self.login()),
            BIND_END_POINT,
            BANK_ID,
            VIEW_ID,
        )

    def send_debin(self, payload: DebinPayload, account_sender_id: str) -> dict:
        return BindService.send_debin(
            payload.to_json(),
            account_sender_id,
            str(self.login()),
            BIND_END_POINT,
            BANK_ID,
            VIEW_ID,
        )

    def get_debins_by_status(self, status: str, account_id: str) -> dict:
        return BindService.get_debins_by_status(
            status,
            account_id,
            str(self.login()),
            BIND_END_POINT,
            BANK_ID,
            VIEW_ID,
        )
