"""
Birman
"""
from typing import Dict


class Decoder:
    """
    Decoder
    """
    data: bytes

    chunk_size = 100

    def __init__(self, data: bytes):
        self.data = data

    def _get_filename(self, field: bytes) -> str:
        fn = field.split(b"name=")[1]
        if b";" in fn:
            fn = fn.split(b";")[0]
        fn = fn.decode("utf-8").strip()
        fn = fn.replace('"', "")
        return fn

    def _get_name(self, field: bytes) -> str:
        n = field.split(b"name=")[1]
        n = n.split(b"\n")[0].decode("utf-8")
        n = n.strip().replace('"', "")
        return n

    def _get_value(self, field: bytes) -> str:
        v = field.split(b"\r\n--")
        v = v[0].split(b"\r\n")
        if len(v) > 0:
            # the last item in the list should contain the value -
            # (normally the 3rd but could be the 2nd
            v = v[len(v)-1]
        else:
            # cannot extract value so return the whole string minus formatting
            return v[0].decode("utf-8").strip()
        if v:
            return v.decode("utf-8").strip()
        return ""

    def decode(self) -> Dict:
        """
        :return: A Dict of multipart formdata fields e.g [name]: [name]: value
        :rtype Optional[Dict]:
        """
        fields = {}
        try:
            assert isinstance(self.data, bytes)
        except AssertionError:
            return {}
        _data_bytes = self.data.split(b"\r\nContent-Disposition")
        if len(_data_bytes) == 0:
            return {}
        data = _data_bytes[1:]
        for d in data:
            # check if the field is a file
            f = d.split(b"filename=")
            if len(f) > 1:
                filename = self._get_filename(f[0])
                value = self._get_filename_value(d)
                fields[filename] = {
                    "name": filename,
                    "value": value,
                    "type": "file",
                }
            else:
                name = self._get_name(f[0])
                value = self._get_value(d)
                fields[name] = {
                    "name": name,
                    "value": value,
                    "type": "text",
                }
        return fields

    def _get_filename_value(self, data: bytes) -> Dict:
        fv = data.split(b"Content-Type")
        if len(fv) < 1:
            fv = data.split(b"content-type")
        filename = fv[0].split(b"filename=")
        filename = filename[1].decode("utf-8").strip()
        filename = filename.replace('"', "")
        mimetype = fv[1].split(b"\r\n")[0]
        byte_str = fv[1].split(mimetype)[1]
        while True:
            if byte_str[:1] == b"\r" or byte_str[:1] == b"\n":
                byte_str = byte_str[2:]
            else:
                break
        # strip mimetype after byte_str work
        mimetype = mimetype.split(b":")[1]
        mimetype = mimetype.decode("utf-8").strip()
        return {
            "filename": filename,
            "mimetype": mimetype,
            "file_data": byte_str,
        }
