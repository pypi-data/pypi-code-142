#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

def sha256_from_file(filepath, blocksize=4096):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        # chunk for long files
        for chunk in iter(lambda: f.read(blocksize), b""):
            hasher.update(chunk)
    return hasher.hexdigest()
