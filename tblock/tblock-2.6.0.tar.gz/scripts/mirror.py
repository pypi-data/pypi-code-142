#!/usr/bin/env python3

# This script helps to mirror all filter lists that are available on
# the filter list repository

import os
import lzma
import tblock

tblock.config.Path.TMP_DIR = "lists/"

if __name__ == "__main__":
    print(f"{tblock.style.Font.BOLD}==> Mirroring filter lists{tblock.style.Font.DEFAULT}")
    if not os.path.isdir(tblock.config.Path.TMP_DIR):
        os.mkdir(tblock.config.Path.TMP_DIR)
    else:
        for i in os.listdir(tblock.config.Path.TMP_DIR):
            os.remove(os.path.join(tblock.config.Path.TMP_DIR, i))
    for f in tblock.get_all_filter_lists(from_repo_only=True):
        filter_id = tblock.Filter(f)
        if filter_id.metadata["license"][0] != "proprietary" and int(filter_id.metadata["warning"]) < 4:
            filter_id.tmp_file
            filter_id.retrieve()
    for f in tblock.get_all_filter_lists(from_repo_only=True):
        filter_id = tblock.Filter(f)
        if filter_id.metadata["license"][0] != "proprietary" and int(filter_id.metadata["warning"]) < 4:
            print(f" {tblock.style.loading_icon(1)} Compressing {filter_id.id} (xz)", end="\r")
            with open(filter_id.tmp_file, "rb") as r:
                compressed = lzma.compress(r.read(), format=lzma.FORMAT_XZ)
            with open(filter_id.tmp_file+".xz", "wb") as w:
                w.write(compressed)
            os.remove(filter_id.tmp_file)
            print(f" {tblock.style.Icon.SUCCESS} Compressing {filter_id.id} (xz)")
