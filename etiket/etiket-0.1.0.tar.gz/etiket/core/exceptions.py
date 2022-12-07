from fastapi import HTTPException, status
from typing import Optional


class IncorrectUsernamePasswordException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Incorrect username or password"
        self.headers = {"WWW-Authenticate": "Bearer"}


class ValidationCredentialsException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Could not validate credentials"
        self.headers = {"WWW-Authenticate": "Bearer"}


class InactiveUserException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Inactive user"


class AdminUserException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "User is not an admin"


class RefreshTokenException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Could not refresh token"


class InvalidRefreshTokenException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Could not refresh token"


class NonExpiredRefreshTokenException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "Do not refresh when access token has not expired"


class AccessTokenUsedAsRefreshTokenException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "Do not use access token to refresh"


class UserNotInScopeException(HTTPException):
    def __init__(self, scope):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = f"You are not part of scope {scope}"


class FileAlreadyExistsException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "Already exists a file with this name for this dataset. If you want to overwrite this file, please upload a new file"


class FileNotAvailableException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "File is not available or secured (yet)"


class InvalidRangeException(HTTPException):
    def __init__(self, Range):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = f"Invalid request range (Range:{Range})"


class UserNotFoundException(HTTPException):
    def __init__(self, username: str):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = (f"User {username} not found",)


class UserAlreadyNotPartOfScopeException(HTTPException):
    def __init__(self, username: str, scope: str):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = (f"{username} is already not part of scope {scope}",)


class UserAlreadyPartOfScopeException(HTTPException):
    def __init__(self, username: str, scope: str):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = (f"{username} is already part of scope {scope}",)


class DatasetAlreadyPartOfCollectionException(HTTPException):
    def __init__(self, scope: str, dataset_uuid, collection):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = f"Dataset within scope {scope} and uuid {dataset_uuid} is already part of collection {collection}"


class DatasetAlreadyNotPartOfCollectionException(HTTPException):
    def __init__(self, scope: str, dataset_uuid, collection):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = f"Dataset within scope {scope} and uuid {dataset_uuid} is already part of collection {collection}"


class UploadStillInProgressException(HTTPException):
    def __init__(self, upload_uuid):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = f"Upload at /uploads/{upload_uuid} still in progress (maybe more). This upload can not be added"


class NotAllUploadsCompletedYetException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "Not all uploads are completed yet"


class IncompleteConcatUUIDListException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "List of UUIDs provided not complete"


class UploadGoneException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_410_GONE
        self.detail = "A part of the upload has been removed"


class ChecksumMismatchException(HTTPException):
    def __init__(self):
        self.status_code = 460
        self.detail = "Checksum mismatch. Need to upload at this offset again"


class DownloadFailedException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = "Download failed. Contact system administrator"


class UploadFailedException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = "Upload failed, please try again"


class UploadTerminationFailedException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = "Termination upload failed, please try again"


class FileIsImmutableException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "File is made immutable and already uploaded"


class NewVersionFileForbiddenException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "No new file version allowed"


class UnsupportedTusVersionException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Unsupported tus protocol version"


class UnsupportedChecksumAlgorithmException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Unsupported checksum algorithm"


class UnsupportedTusExtensionException(HTTPException):
    def __init__(self, extension: str):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = f"Unsupported tus extension: no {extension}"


class UploadLengthException(HTTPException):
    def __init__(self, size: int):
        self.status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
        self.detail = f"Upload length for (partial) upload larger than {size}"


class UploadOffsetMismatchException(HTTPException):
    def __init__(self, size: int):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = "Offset of upload provided not the same as stored"


class UploadAlreadyCompletedException(HTTPException):
    def __init__(self, size: int):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = "Upload is already completed. Can not be continued"


class ContentTypeException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Content-Type needs to be application/offset+octet-stream"


class DeferUploadLengthException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "No upload length provided. Cannot be deffered."


class ContentLengthLargerThanUploadLengthException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Provided content length larger than provided upload length"


class UploadChecksumHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Incorrect Upload-Checksum header"


class UploadUUIDInConcatHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Not a valid file UUID in Upload-Concat final header"


class UploadConcatHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Something went wrong while parsing Upload-Concat final header"


class UploadLengthInFinalConcatHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Upload length defined for final request for concatenation"


class UploadMetadataHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Invalid Upload-Metadata header"


class MissingScopeUploadMetadataHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "No scope defined in Upload-Metadata"


class MissingFileUUIDUploadMetadataHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "No file UUID defined in Upload-Metadata"


class InvalidFileUUIDUploadMetadataHeaderException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Not a valid file UUID in Upload-Metadata"
