import requests

from ..Notifier import Notifier


class TelegramNotifier(Notifier):
    def send(self, msg, attachments={}):
        """
        .. seealso:: Notifier.send()
        """
        telegram_url = "https://api.telegram.org/bot{}".format(
            self._config.get("telegram_token")
        )
        chat_id = self._config.get("telegram_chat_id")
        requests.post(
            "{}/sendMessage".format(telegram_url),
            data={
                "text": msg,
                "parse_mode": "MARKDOWN",
                "chat_id": chat_id,
            },
        )

        for filename, content in attachments.items():
            requests.post(
                "{}/sendDocument".format(telegram_url),
                files={"document": (filename, content)},
                data={
                    "chat_id": chat_id,
                },
            )
