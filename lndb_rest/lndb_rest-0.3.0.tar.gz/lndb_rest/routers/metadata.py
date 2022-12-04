from fastapi import APIRouter
from lndb_setup import settings

router = APIRouter(prefix="/metadata")


@router.get("/")
def get_metadata():
    return {
        "name": settings.instance.name,
        "db": settings.instance.db,
        "storage_root": settings.instance.storage_root,
        "storage_region": settings.instance.storage_region,
        "_dbconfig": settings.instance._dbconfig,
        "schema_modules": settings.instance.schema_modules,
    }
