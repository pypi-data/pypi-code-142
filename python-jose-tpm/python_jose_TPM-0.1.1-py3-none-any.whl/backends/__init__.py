try:
    from python_jose_TPM.backends.cryptography_backend import get_random_bytes  # noqa: F401
except ImportError:
    try:
        from python_jose_TPM.backends.pycrypto_backend import get_random_bytes  # noqa: F401
    except ImportError:
        from python_jose_TPM.backends.native import get_random_bytes  # noqa: F401

try:
    from python_jose_TPM.backends.cryptography_backend import CryptographyRSAKey as RSAKey  # noqa: F401
except ImportError:
    try:
        from python_jose_TPM.backends.rsa_backend import RSAKey  # noqa: F401
    except ImportError:
        RSAKey = None

try:
    from python_jose_TPM.backends.cryptography_backend import CryptographyECKey as ECKey  # noqa: F401
except ImportError:
    from python_jose_TPM.backends.ecdsa_backend import ECDSAECKey as ECKey  # noqa: F401

try:
    from python_jose_TPM.backends.cryptography_backend import CryptographyAESKey as AESKey  # noqa: F401
except ImportError:
    AESKey = None

try:
    from python_jose_TPM.backends.cryptography_backend import CryptographyHMACKey as HMACKey  # noqa: F401
except ImportError:
    from python_jose_TPM.backends.native import HMACKey  # noqa: F401

from .base import DIRKey  # noqa: F401
