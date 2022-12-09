from io import BytesIO

def convert_kwargs(**kwargs):
    converted_kwargs = {
    }
    if 'files' in kwargs:
        files = kwargs.get('files')
        files_data = (b"")
        for _file in files:
            if files_data:
                files_data += (b"\r\n")
            files_data += (b"--boundary\r\n")
            files_data += (b'Content-Disposition: form-data; name="') + _file.encode() + (b'"; filename="') + files.get(_file).name.encode() + (b'"\r\n')
            files_data += (b"\r\n")
            files_data += files.get(_file).read()
            files_data += (b"\r\n")
            files_data += (b"--boundary--")

    if 'files' in kwargs:
        converted_kwargs['input_stream'] =  BytesIO(files_data)
        converted_kwargs['content_type'] = "multipart/form-data; boundary=boundary"
        converted_kwargs['content_length'] = len(files_data)

    for key, value in kwargs.items():
        if key in ['method', 'url', 'files', 'data', 'json', 'params', 'cookies']:
            continue
        converted_kwargs[key] = value
    return converted_kwargs
