import boto3
from fastapi import HTTPException

from etiket.core.config import settings


def get_s3_client():

    try:
        s3 = boto3.Session(profile_name="default")
        s3_client = s3.client(
            "s3",
            endpoint_url=settings.S3_ENDPOINT,
            use_ssl=True,
            verify=True,
        )
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Could not get connection to storage device",
        )

    return s3_client


def get_s3_bucket_name():
    return settings.S3_BUCKET


def get_s3_prefix():
    return settings.S3_PREFIX


def get_s3_expiration():
    return settings.S3_PRESIGN_EXPIRATION


def get_s3_part_size():
    return settings.S3_MULTIPART_UPLOAD_PARTSIZE


def get_s3_max_number_parts():
    return settings.S3_MAX_NUMBER_PARTS


def get_s3_stream_number_parts():
    return settings.S3_STREAM_NUMBER_OF_PARTS


def get_s3_max_part_size():
    return settings.S3_MAX_PART_SIZE


def get_s3_min_part_size():
    return settings.S3_MIN_PART_SIZE


def get_s3_singlepart_size_limit():
    return settings.S3_SINGLEPART_SIZE_LIMIT


def get_s3_etag(s3etag: str):
    return s3etag.replace('"', "")


def get_number_of_parts_from_etag(etag: str):

    etagsplitted = etag.split("-")
    if len(etagsplitted) == 1:
        return None
    else:
        return int(etagsplitted[1].replace('"', ""))


def get_s3_key(scope,file_uuid):
    return f"{settings.S3_PREFIX}/{scope}/{file_uuid}"


def get_s3_object_name(s3prefix, dataset_id, file_name, file_id):
    return f"{s3prefix}/datasets/{dataset_id}/files/{file_name}/{file_id}"


def check_s3_object_integrity(
    bucket_name, object_name, etag_client, size_client, s3_client=None
):

    response = head_s3_object(bucket_name, object_name, s3_client=s3_client)
    etag = response.get("ETag")
    etag = get_s3_etag(etag)
    if etag != etag_client:
        raise HTTPException(
            status_code=409,
            detail=f"Warning: provided etag does not correspond to stored etag of file",
        )
    size = response["ContentLength"]
    if size != size_client:
        raise HTTPException(
            status_code=409,
            detail=f"Warning: provided size does not correspond to stored size of file",
        )


def abort_multipart_upload(
    bucket_name: str, object_name: str, upload_id: str, s3_client=None
):

    try:
        response = s3_client.abort_multipart_upload(
            Bucket=bucket_name, Key=object_name, UploadId=upload_id
        )
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Could not abort multipart upload",
        )

    return response


def list_multipart_uploads(bucket_name: str, object_name: str, s3_client=None):

    try:
        response = s3_client.list_multipart_uploads(
            Bucket=bucket_name,
            Prefix=object_name,
        )
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Could not list multipart uploads",
        )

    return response


def head_s3_object(bucket_name: str, object_name: str, s3_client=None):

    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=object_name)
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Could not find data object with name {object_name}",
        )

    return response


def create_multipart_upload(bucket_name: str, object_name: str, s3_client=None):

    try:
        response = s3_client.create_multipart_upload(
            Bucket=bucket_name, Key=object_name
        )
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Could not create multipart upload",
        )

    return response


def complete_multipart_upload(
    bucket_name: str, object_name: str, upload_id: str, parts: list, s3_client=None
):

    try:
        response = s3_client.complete_multipart_upload(
            Bucket=bucket_name,
            Key=object_name,
            MultipartUpload={"Parts": parts},
            UploadId=upload_id,
        )
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Could not complete multipart upload",
        )

    return response


def get_keys_from_presigned_url(presigned_url: str):

    path, pathparams = presigned_url.split("?")
    pathparams = [x.split("=") for x in pathparams.split("&")]
    pathparams = [item for sublist in pathparams for item in sublist]
    pathparams = {
        pathparams[i]: pathparams[i + 1] for i in range(0, len(pathparams), 2)
    }
    pathparams["UrlPath"] = path

    return pathparams


def get_presigned_url_keys(
    method: str = None,
    bucket_name: str = None,
    object_name: str = None,
    upload_id: str = None,
    part_number: int = None,
    expiration: int = None,
    s3_client=None,
):

    params = {
        "Bucket": bucket_name,
        "Key": object_name,
    }
    if method == "upload_part":
        params["UploadId"] = upload_id
        params["PartNumber"] = part_number
    elif method == "get_object_part":
        method = "get_object"
        params["PartNumber"] = part_number

    try:
        presigned_url = s3_client.generate_presigned_url(
            ClientMethod=method, Params=params, ExpiresIn=expiration
        )
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Could not get generate safe link from storage device",
        )

    return get_keys_from_presigned_url(presigned_url)
