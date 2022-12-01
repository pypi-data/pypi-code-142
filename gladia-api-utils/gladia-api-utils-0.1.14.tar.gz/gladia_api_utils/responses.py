from fastapi.responses import Response


class ImageResponse(Response):
    """
    Image response class for fastapi
    """

    media_type = "image/*"

    schema = {"type": "string", "format": "binary", "data_type": "image"}


class AudioResponse(Response):
    """
    Audio response class for fastapi
    """

    media_type = "audio/*"

    schema = {"type": "string", "format": "binary", "data_type": "audio"}


class VideoResponse(Response):
    """
    Video response class for fastapi
    """

    media_type = "video"

    schema = {"type": "string", "format": "binary", "data_type": "video"}
