import base64
import hmac
import hashlib


def sign(source, secret):
    h = hmac.new(secret.encode('utf-8'), source.encode('utf-8'), digestmod=hashlib.sha256).digest()
    signature = str(base64.b64encode(h), 'utf-8')
    return signature
