import binascii
import json
from collections.abc import Iterable, Mapping

from tpm2_pytss import TPMT_SIGNATURE, TPM2_ALG, TPMT_TK_VERIFIED, TPM2B_PUBLIC_KEY_RSA, TPMS_SIGNATURE_RSA, ESYS_TR, \
    TPMU_SIGNATURE, TPM2B_DIGEST, TPM2_ST, TPMT_TK_HASHCHECK, TPM2_RH, TPMT_SIG_SCHEME, TPM2B_MAX_BUFFER
from tpm2_pytss._libtpm2_pytss.lib import TPM2_MAX_DIGEST_BUFFER

from python_jose_TPM import jwk
from python_jose_TPM.backends.base import Key
from python_jose_TPM.constants import ALGORITHMS
from python_jose_TPM.exceptions import JWSError, JWSSignatureError
from python_jose_TPM.utils import base64url_decode, base64url_encode


def sign(payload, esapi, key_handle, headers=None, algorithm=ALGORITHMS.RS256):
    """Signs a claims set and returns a JWS string.

    Args:
        payload (str or dict): A string to sign
        esapi (ESAPI): The TPM ESAPI to use
        key_handle (ESYS_TR): The key handle to use for signing the claim set.
        headers (dict, optional): A set of headers that will be added to
            the default headers.  Any headers that are added as additional
            headers will override the default headers.
        algorithm (str, optional): The algorithm to use for signing the
            claims. Defaults to RS256.

    Returns:
        str: The string representation of the header, claims, and signature.

    Raises:
        JWSError: If there is an error signing the token.
    """

    if algorithm is not ALGORITHMS.RS256:
        raise JWSError("Algorithm %s not supported." % algorithm)

    encoded_header = _encode_header(algorithm, additional_headers=headers)
    encoded_payload = _encode_payload(payload)
    signed_output = _sign_header_and_claims(encoded_header, encoded_payload, algorithm, esapi, key_handle)

    return signed_output


def verify(token, esapi, key_handle, algorithms=ALGORITHMS.RS256, verify=True):
    """Verifies a JWS string's signature.

    Args:
        token (str): A signed JWS to be verified.
        esapi (ESAPI): The TPM ESAPI to use
        key_handle (ESYS_TR): The key handle to use for verifying the token signature.
        algorithms (str or list): Valid algorithms that should be used to verify the JWS.

    Returns:
        str: The str representation of the payload, assuming the signature is valid.

    Raises:
        JWSError: If there is an exception verifying a token.
    """

    header, payload, signing_input, signature = _load(token)

    if verify:
        _verify_signature(signing_input, header, signature, esapi, key_handle, algorithms)

    return payload


def get_unverified_header(token):
    """Returns the decoded headers without verification of any kind.

    Args:
        token (str): A signed JWS to decode the headers from.

    Returns:
        dict: The dict representation of the token headers.

    Raises:
        JWSError: If there is an exception decoding the token.
    """
    header, claims, signing_input, signature = _load(token)
    return header


def get_unverified_headers(token):
    """Returns the decoded headers without verification of any kind.

    This is simply a wrapper of get_unverified_header() for backwards
    compatibility.

    Args:
        token (str): A signed JWS to decode the headers from.

    Returns:
        dict: The dict representation of the token headers.

    Raises:
        JWSError: If there is an exception decoding the token.
    """
    return get_unverified_header(token)


def get_unverified_claims(token):
    """Returns the decoded claims without verification of any kind.

    Args:
        token (str): A signed JWS to decode the headers from.

    Returns:
        str: The str representation of the token claims.

    Raises:
        JWSError: If there is an exception decoding the token.
    """
    header, claims, signing_input, signature = _load(token)
    return claims


def _encode_header(algorithm, additional_headers=None):
    header = {"typ": "JWT", "alg": algorithm}

    if additional_headers:
        header.update(additional_headers)

    json_header = json.dumps(
        header,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    return base64url_encode(json_header)


def _encode_payload(payload):
    if isinstance(payload, Mapping):
        try:
            payload = json.dumps(
                payload,
                separators=(",", ":"),
            ).encode("utf-8")
        except ValueError:
            pass

    return base64url_encode(payload)


def _sign_header_and_claims(encoded_header, encoded_claims, algorithm, esapi, key_handle):
    signing_input = b".".join([encoded_header, encoded_claims])
    if algorithm == ALGORITHMS.RS256:
        try:
            chunks = [signing_input[i:i + TPM2_MAX_DIGEST_BUFFER] for i in range(0, len(signing_input), TPM2_MAX_DIGEST_BUFFER)]
            seq_handle = esapi.hash_sequence_start(None, TPM2_ALG.SHA256)
            for chunk in chunks:
                esapi.sequence_update(seq_handle, chunk)
            hashed_input, _ = esapi.sequence_complete(seq_handle, "")
            scheme = TPMT_SIG_SCHEME(scheme=TPM2_ALG.RSASSA)
            scheme.details.rsassa.hashAlg = TPM2_ALG.SHA256

            # create a NULL ticket which must be used when the key is not restricted
            validation = TPMT_TK_HASHCHECK(tag=TPM2_ST.HASHCHECK, hierarchy=TPM2_RH.OWNER)
            signature = esapi.sign(key_handle, TPM2B_DIGEST(hashed_input), in_scheme=scheme, validation=validation)
        except Exception as e:
            raise JWSError(e)
    else:
        raise JWSError("Invalid or unsupported algorithm: %s" % algorithm)

    encoded_signature = base64url_encode(bytes(signature.signature.rsassa.sig))
    encoded_string = b".".join([encoded_header, encoded_claims, encoded_signature])
    return encoded_string.decode("utf-8")


def _load(jwt):
    if isinstance(jwt, str):
        jwt = jwt.encode("utf-8")
    try:
        signing_input, crypto_segment = jwt.rsplit(b".", 1)
        header_segment, claims_segment = signing_input.split(b".", 1)
        header_data = base64url_decode(header_segment)
        claims_data = base64url_decode(claims_segment)
    except ValueError:
        raise JWSError("Not enough segments")
    except (TypeError, binascii.Error):
        raise JWSError("Invalid header padding")

    try:
        header = json.loads(header_data.decode("utf-8"))
    except ValueError as e:
        raise JWSError("Invalid header string: %s" % e)

    if not isinstance(header, Mapping):
        raise JWSError("Invalid header string: must be a json object")

    try:
        payload = claims_data.decode("utf-8")
    except (TypeError, binascii.Error):
        raise JWSError("Invalid payload padding")

    try:
        signature = base64url_decode(crypto_segment)
    except (TypeError, binascii.Error):
        raise JWSError("Invalid crypto padding")

    return header, payload, signing_input, signature


def _verify_signature(signing_input, header, signature, esapi, key_handle, algorithms):
    alg = header.get("alg")
    if not alg:
        raise JWSError("No algorithm was specified in the JWS header.")
    if algorithms is not ALGORITHMS.RS256:
        raise JWSError("The specified alg value is not supported")
    try:
        chunks = [signing_input[i:i + TPM2_MAX_DIGEST_BUFFER] for i in range(0, len(signing_input), TPM2_MAX_DIGEST_BUFFER)]
        seq_handle = esapi.hash_sequence_start(None, TPM2_ALG.SHA256)
        for chunk in chunks:
            esapi.sequence_update(seq_handle, chunk)
        hashed_input, _ = esapi.sequence_complete(seq_handle, "")
        sig = TPMT_SIGNATURE(sigAlg=TPM2_ALG.RSASSA,
                             signature=TPMU_SIGNATURE(rsassa=TPMS_SIGNATURE_RSA(hash=TPM2_ALG.SHA256,
                                                                                sig=TPM2B_PUBLIC_KEY_RSA(
                                                                                    buffer=signature))))
        verification_result = esapi.verify_signature(key_handle=key_handle, digest=hashed_input, signature=sig)
        if not isinstance(verification_result, TPMT_TK_VERIFIED):
            raise JWSSignatureError()
    except JWSSignatureError:
        raise JWSError("Signature verification failed.")
    except JWSError:
        raise JWSError("Invalid or unsupported algorithm: %s" % algorithms)
