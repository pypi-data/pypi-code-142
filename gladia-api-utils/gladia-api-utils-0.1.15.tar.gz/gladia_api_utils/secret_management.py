import os
from logging import getLogger
from warnings import warn

logger = getLogger(__name__)


class SecretManager:
    """
    SecretManager is a class that allows to access secrets in a safe way.

    Args:
        secrets (dict): Dictionary of secrets.

    Examples:
        >>> SECRETS['SECRET_KEY']
        'secret'

    """

    __secrets = {
        "HUGGINGFACE_ACCESS_TOKEN": {
            "value": os.getenv("HUGGINGFACE_ACCESS_TOKEN"),
            "error_message": "HUGGINGFACE_ACCESS_TOKEN environement variable was not set, please visite hugging-face's web site to retrieve your access token : (https://huggingface.co/settings/tokens) (https://huggingface.co/docs/hub/security-tokens/)",
        },
        "STABILITY_KEY": {
            "value": os.getenv("STABILITY_KEY"),
            "error_message": "STABILITY_KEY environement variable was not set, please visite dream studio's web site to retrieve your access token : (https://beta.dreamstudio.ai/membership)",
        },
    }

    def __getitem__(self, item):
        """
        Get a secret value.

        Args:
            item (str): Name of the secret to retrive.

        Returns:
            str: Value of the secret.

        Raises:
            RuntimeError: If the secret is not found.
        """

        if item not in self.__secrets:
            error_message = f"{item} is not set in the SecretManager."

            logger.error(error_message)
            raise RuntimeError(error_message)

        if self.__secrets[item]["value"] is None:
            warn(self.__secrets[item]["error_message"])

            return None

        return self.__secrets[item]["value"]


SECRETS = SecretManager()
