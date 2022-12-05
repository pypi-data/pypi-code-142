# (c) 2017 Microchip Technology Inc. and its subsidiaries.  You may use this
# software and any derivatives exclusively with Microchip products.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS".  NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
# PURPOSE, OR ITS INTERACTION WITH MICROCHIP PRODUCTS, COMBINATION WITH ANY
# OTHER PRODUCTS, OR USE IN ANY APPLICATION.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE.  TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
#
# MICROCHIP PROVIDES THIS SOFTWARE CONDITIONALLY UPON YOUR ACCEPTANCE OF THESE
# TERMS.

import os
import cryptography
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec


def load_or_create_key(crypto_be, filename, verbose=True):
    # Create or load a root CA key pair
    priv_key = None
    if os.path.isfile(filename):
        # Load existing key
        with open(filename, 'rb') as f:
            if verbose:
                print('    Loading from ' + f.name)
            priv_key = serialization.load_pem_private_key(
                data=f.read(),
                password=None,
                backend=crypto_be)
    if priv_key is None:
        # No private key loaded, generate new one
        if verbose:
            print('    No key file found, generating new key')
        priv_key = ec.generate_private_key(ec.SECP256R1(), crypto_be)
        # Save private key to file
        with open(filename, 'wb') as f:
            if verbose:
                print('    Saving to ' + f.name)
            pem_key = priv_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption())
            f.write(pem_key)
    return priv_key


def random_cert_sn(size):
    """Create a positive, non-trimmable serial number for X.509 certificates"""
    raw_sn = bytearray(os.urandom(size))
    raw_sn[0] = raw_sn[0] & 0x7F  # Force MSB bit to 0 to ensure positive integer
    raw_sn[0] = raw_sn[0] | 0x40  # Force next bit to 1 to ensure the integer won't be trimmed in ASN.1 DER encoding
    return int.from_bytes(raw_sn, byteorder='big', signed=False)


def pubkey_cert_sn(size, builder):
    """Cert serial number is the SHA256(Subject public key + Encoded dates)"""

    # Get the public key as X and Y integers concatenated
    pub_nums = builder._public_key.public_numbers()
    pubkey =  pub_nums.x.to_bytes(32, byteorder='big', signed=False)
    pubkey += pub_nums.y.to_bytes(32, byteorder='big', signed=False)

    # Get the encoded dates
    expire_years = builder._not_valid_after.year - builder._not_valid_before.year
    if builder._not_valid_after.year == 9999:
        expire_years = 0  # This year is used when indicating no expiration
    elif expire_years > 31:
        expire_years = 1  # We default to 1 when using a static expire beyond 31

    enc_dates = bytearray(b'\x00' * 3)
    enc_dates[0] = (enc_dates[0] & 0x07) | ((((builder._not_valid_before.year - 2000) & 0x1F) << 3) & 0xFF)
    enc_dates[0] = (enc_dates[0] & 0xF8) | ((((builder._not_valid_before.month) & 0x0F) >> 1) & 0xFF)
    enc_dates[1] = (enc_dates[1] & 0x7F) | ((((builder._not_valid_before.month) & 0x0F) << 7) & 0xFF)
    enc_dates[1] = (enc_dates[1] & 0x83) | (((builder._not_valid_before.day & 0x1F) << 2) & 0xFF)
    enc_dates[1] = (enc_dates[1] & 0xFC) | (((builder._not_valid_before.hour & 0x1F) >> 3) & 0xFF)
    enc_dates[2] = (enc_dates[2] & 0x1F) | (((builder._not_valid_before.hour & 0x1F) << 5) & 0xFF)
    enc_dates[2] = (enc_dates[2] & 0xE0) | ((expire_years & 0x1F) & 0xFF)
    enc_dates = bytes(enc_dates)

    # SAH256 hash of the public key and encoded dates
    digest = hashes.Hash(hashes.SHA256(), backend=cryptography.hazmat.backends.default_backend())
    digest.update(pubkey)
    digest.update(enc_dates)
    raw_sn = bytearray(digest.finalize()[:size])
    raw_sn[0] = raw_sn[0] & 0x7F  # Force MSB bit to 0 to ensure positive integer
    raw_sn[0] = raw_sn[0] | 0x40  # Force next bit to 1 to ensure the integer won't be trimmed in ASN.1 DER encoding
    return int.from_bytes(raw_sn, byteorder='big', signed=False)


def is_key_file_password_protected(crypto_be, key_filename):
    try:
        with open(key_filename, 'rb') as f:
            serialization.load_pem_private_key(data=f.read(), password=None, backend=crypto_be)
        return False
    except TypeError:
        return True
