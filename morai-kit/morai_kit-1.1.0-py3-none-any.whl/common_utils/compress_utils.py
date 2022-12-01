import gzip
import base64

def decompress(compressed, base64_encoded = True):
    source = compressed
    if base64_encoded:
        source = base64.standard_b64decode(compressed)

    return gzip.decompress(source).decode('utf-8')
