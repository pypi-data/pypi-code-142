from typing import List, Optional
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import (
    Request,
    Depends,
    Query,
    Header,
    Form,
    Path,
    Response,
    APIRouter,
)
from sqlmodel import Session
from uuid import UUID

from etiket.app.models import *
from etiket.app.services import (
    TokenService,
    ScopeService,
    UserService,
    CollectionService,
    DatasetService,
    FileService,
    TusService,
)
from etiket.app.crud.db import get_session
from etiket.core.security import (
    get_refreshed_active_user,
    get_current_active_adminuser,
    get_current_active_user,
)


router = APIRouter()


@router.post("/token", response_model=Token, tags=["access"])
async def login_for_access_token(
    *,
    session: Session = Depends(get_session),
    form_data: OAuth2PasswordRequestForm = Depends(),
):

    return await TokenService().get_tokens(form_data, session)


@router.post("/refresh", response_model=Token, tags=["access"])
async def refresh_token(
    refreshed_user: User = Depends(get_refreshed_active_user),
):

    return await TokenService().refresh_tokens(refreshed_user.username)


@router.post("/scopes/", response_model=ScopeRead, tags=["admin"])
async def create_scope(
    *,
    session: Session = Depends(get_session),
    scope: ScopeCreate,
    current_user: User = Depends(get_current_active_adminuser),
):

    return await ScopeService().create_scope(scope, session)


@router.get("/scopes/", response_model=List[ScopeRead], tags=["admin"])
async def get_scopes(
    *,
    session: Session = Depends(get_session),
    name: Optional[str] = Query(None, min_length=3, max_length=100),
    offset: int = 0,
    limit: int = Query(default=800, lte=1000),
    current_user: User = Depends(get_current_active_user),
):
    return await ScopeService().get_scopes(name, offset, limit, session)


@router.get("/scopes/{name}", response_model=ScopeRead, tags=["admin"])
async def get_scope(
    *,
    session: Session = Depends(get_session),
    name: str = Path(..., min_length=3, max_length=100),
    current_user: User = Depends(get_current_active_user),
):
    return await ScopeService().get_scope(name, session)


@router.patch("/scopes/{name}", response_model=ScopeRead, tags=["admin"])
async def update_scope(
    *,
    session: Session = Depends(get_session),
    name: str,
    scope: ScopeUpdate,
    current_user: User = Depends(get_current_active_adminuser),
):
    return await ScopeService().update_scope(name, scope, session)


@router.put(
    "/scopes/{scope}/members/{newusername}", response_model=ScopeRead, tags=["admin"]
)
async def add_user_to_scope(
    *,
    session: Session = Depends(get_session),
    scope: str,
    newusername: str,
    current_user: User = Depends(get_current_active_user),
):

    return await ScopeService().add_user_to_scope(
        scope, newusername, current_user, session
    )


@router.delete(
    "/scopes/{scope}/members/{username}", response_model=ScopeRead, tags=["admin"]
)
async def remove_user_from_scope(
    *,
    session: Session = Depends(get_session),
    scope: str,
    username: str,
    current_user: User = Depends(get_current_active_adminuser),
):

    return await ScopeService().remove_user_from_scope(scope, username, session)


@router.post("/users/", response_model=UserReadExtended, tags=["admin"])
async def create_user(
    *,
    session: Session = Depends(get_session),
    user: UserCreate,
    current_user: User = Depends(get_current_active_adminuser),
):

    return await UserService().create_user(user, session)


@router.get("/users/", response_model=List[UserReadExtended], tags=["admin"])
async def get_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=800, lte=1000),
    current_user: User = Depends(get_current_active_user),
):

    return await UserService().get_users(offset, limit, session)


@router.get("/users/me", response_model=UserReadExtended, tags=["admin"])
async def get_userme(
    *,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user),
):

    return current_user


@router.get("/users/{username}", response_model=UserRead, tags=["admin"])
async def get_user(
    *,
    session: Session = Depends(get_session),
    username: str,
    current_user: User = Depends(get_current_active_user),
):

    return await UserService().get_user(username, session)


@router.patch("/users/{username}", response_model=UserRead, tags=["admin"])
async def update_user(
    *,
    session: Session = Depends(get_session),
    username: str,
    user: UserUpdate,
    current_user: User = Depends(get_current_active_adminuser),
):

    return await UserService().get_user(username, session)


@router.post(
    "/collections/", response_model=CollectionReadExtended, tags=["collections"]
)
async def create_collection(
    *,
    session: Session = Depends(get_session),
    collection: CollectionCreate,
    current_user: User = Depends(get_current_active_user),
):

    return await CollectionService().create_collection(
        collection, current_user, session
    )


@router.get("/collections/", response_model=List[CollectionRead], tags=["collections"])
async def get_collections(
    *,
    session: Session = Depends(get_session),
    scope: Optional[str] = Query(..., min_length=3, max_length=100),
    name: Optional[str] = Query(None, min_length=3, max_length=100),
    offset: int = 0,
    limit: int = Query(default=800, lte=1000),
    current_user: User = Depends(get_current_active_user),
):

    return await CollectionService().get_collections(
        scope, name, offset, limit, session
    )


@router.get(
    "/collections/{scope}/{name}",
    response_model=CollectionReadExtended,
    tags=["collections"],
)
async def get_collection(
    *,
    session: Session = Depends(get_session),
    scope: str,
    name: str,
    current_user: User = Depends(get_current_active_user),
):

    return await CollectionService().get_collection(scope, name, session)


@router.put(
    "/collections/{scope}/{name}/datasets/{dataset_uuid}",
    response_model=CollectionReadExtended,
    tags=["collections"],
)
async def add_dataset_to_collection(
    *,
    session: Session = Depends(get_session),
    scope: str,
    name: str,
    dataset_uuid: UUID,
    current_user: User = Depends(get_current_active_user),
):

    return await CollectionService().add_dataset_to_collection(
        scope, name, dataset_uuid, current_user, session
    )


@router.delete(
    "/collections/{scope}/{name}/datasets/{dataset_uuid}",
    response_model=CollectionReadExtended,
    tags=["collections"],
)
async def remove_dataset_from_collection(
    *,
    session: Session = Depends(get_session),
    scope: str,
    name: str,
    dataset_uuid: UUID,
    current_user: User = Depends(get_current_active_user),
):

    return await CollectionService().remove_dataset_from_collection(
        scope, name, dataset_uuid, current_user, session
    )


@router.patch(
    "/collections/{scope}/{name}",
    response_model=CollectionReadExtended,
    tags=["collections"],
)
async def update_collection(
    *,
    session: Session = Depends(get_session),
    scope: str,
    name: str,
    collection: CollectionUpdate,
    current_user: User = Depends(get_current_active_user),
):

    return await CollectionService().update_collection(
        scope, name, collection, current_user, session
    )


@router.post("/datasets/", response_model=DatasetReadExtended, tags=["datasets"])
async def create_dataset(
    *,
    session: Session = Depends(get_session),
    dataset: DatasetWithFilesCreate,
    current_user: User = Depends(get_current_active_user),
):

    return await DatasetService().create_dataset(dataset, current_user, session)


@router.get("/datasets/", response_model=List[DatasetReadExtended], tags=["datasets"])
async def get_datasets(
    *,
    session: Session = Depends(get_session),
    scope: Optional[str] = Query(..., min_length=3, max_length=100),
    collection: Optional[str] = Query(None, min_length=3, max_length=100),
    name: Optional[str] = Query(None, min_length=3, max_length=100),
    since: Optional[datetime] = Query(None),
    until: Optional[datetime] = Query(None),
    offset: int = 0,
    limit: int = Query(default=500, lte=1000),
    current_user: User = Depends(get_current_active_user),
):

    return await DatasetService().get_datasets(
        scope, collection, name, since, until, offset, limit, session
    )


@router.get(
    "/datasets/{scope}/{dataset_uuid}",
    response_model=DatasetReadExtended,
    tags=["datasets"],
)
async def get_dataset(
    *,
    session: Session = Depends(get_session),
    scope: str,
    dataset_uuid: UUID,
    current_user: User = Depends(get_current_active_user),
):

    return await DatasetService().get_dataset(scope, dataset_uuid, session)


@router.patch(
    "/datasets/{scope}/{dataset_uuid}",
    response_model=DatasetReadExtended,
    tags=["datasets"],
)
async def update_dataset(
    *,
    session: Session = Depends(get_session),
    scope: str,
    dataset_uuid: UUID,
    dataset: DatasetUpdate,
    current_user: User = Depends(get_current_active_user),
):

    return await DatasetService().update_dataset(
        scope, dataset_uuid, dataset, current_user, session
    )


@router.post(
    "/metadata/{scope}/{dataset_uuid}",
    response_model=DatasetReadExtended,
    tags=["datasets"],
)
async def add_metadata(
    *,
    session: Session = Depends(get_session),
    scope: str,
    dataset_uuid: UUID,
    add_meta: DatasetMeta,
    current_user: User = Depends(get_current_active_user),
):

    return await DatasetService().add_metadata_to_dataset(
        scope, dataset_uuid, add_meta, current_user, session
    )


@router.put(
    "/metadata/{scope}/{dataset_uuid}",
    response_model=DatasetReadExtended,
    tags=["datasets"],
)
async def set_metadata(
    *,
    session: Session = Depends(get_session),
    scope: str,
    dataset_uuid: UUID,
    set_meta: DatasetMeta,
    current_user: User = Depends(get_current_active_user),
):

    return await DatasetService().set_metadata_for_dataset(
        scope, dataset_uuid, set_meta, current_user, session
    )


@router.delete(
    "/metadata/{scope}/{dataset_uuid}",
    response_model=DatasetReadExtended,
    tags=["datasets"],
)
async def delete_metadata(
    *,
    session: Session = Depends(get_session),
    scope: str,
    dataset_uuid: UUID,
    del_meta: DatasetMetaKeys,
    current_user: User = Depends(get_current_active_user),
):

    return await DatasetService().delete_metadata_from_dataset(
        scope, dataset_uuid, del_meta, current_user, session
    )


@router.post("/files/", response_model=FileRead, tags=["datasets"])
async def add_file(
    *,
    session: Session = Depends(get_session),
    file: FileCreate,
    current_user: User = Depends(get_current_active_user),
):

    return await FileService().add_file(file, current_user, session)


@router.patch("/files/{scope}/{file_uuid}", response_model=FileRead, tags=["datasets"])
async def update_file(
    *,
    session: Session = Depends(get_session),
    scope: str,
    file_uuid: UUID,
    file: FileUpdate,
    current_user: User = Depends(get_current_active_user),
):

    return await FileService().update_file(
        scope, file_uuid, file, current_user, session
    )


@router.get("/files/{scope}/{file_uuid}", tags=["datasets"])
async def get_file(
    *,
    session: Session = Depends(get_session),
    scope: str,
    file_uuid: UUID,
    Range: Optional[str] = Header(default=None, regex="^bytes="),
    current_user: User = Depends(get_current_active_user),
):
    # check if scope is restricted or not, probably needs to go in the dependency
    # also allow for ranged header for parallel download

    return await FileService().get_file(scope, file_uuid, Range, current_user, session)


@router.options("/uploads/", tags=["tus"])
async def options_upload(
    current_user: User = Depends(get_current_active_user),
):

    return TusService().options_upload()


@router.post("/uploads/", tags=["tus"])
async def start_upload(
    *,
    session: Session = Depends(get_session),
    response: Response,
    request: Request,
    upload_length: int = Header(default=None, gt=0),
    tus_resumable: str = Header(...),
    upload_metadata: str = Header(...),
    content_length: int = Header(..., ge=0),
    content_type: Optional[str] = Header(default=None),
    upload_concat: Optional[str] = Header(default=None),
    upload_defer_length: Optional[int] = Header(default=None),
    upload_checksum: Optional[str] = Header(default=None),
    current_user: User = Depends(get_current_active_user),
):

    return await TusService().start_upload(
        tus_resumable,
        upload_length,
        upload_metadata,
        content_length,
        content_type,
        upload_concat,
        upload_defer_length,
        upload_checksum,
        request,
        current_user,
        session,
    )


@router.head("/uploads/{upload_uuid}", tags=["tus"])
async def status_upload(
    *,
    session: Session = Depends(get_session),
    response: Response,
    upload_uuid: UUID,
    tus_resumable: str = Header(...),
    current_user: User = Depends(get_current_active_user),
):

    return await TusService().status_upload(
        tus_resumable, upload_uuid, current_user, session
    )


@router.patch("/uploads/{upload_uuid}", tags=["tus"])
async def continue_upload(
    *,
    session: Session = Depends(get_session),
    response: Response,
    request: Request,
    upload_uuid: UUID,
    tus_resumable: str = Header(...),
    content_length: int = Header(..., gt=0),
    content_type: str = Header(...),
    upload_offset: int = Header(..., ge=0),
    upload_checksum: Optional[str] = Header(default=None),
    current_user: User = Depends(get_current_active_user),
):

    return await TusService().continue_upload(
        upload_uuid,
        tus_resumable,
        upload_offset,
        content_length,
        content_type,
        upload_checksum,
        request,
        current_user,
        session,
    )


@router.delete("/uploads/{upload_uuid}", tags=["tus"])
async def terminate_upload(
    *,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user),
    upload_uuid: UUID,
):

    return await TusService().terminate_upload(upload_uuid, current_user, session)
