from fastapi import FastAPI
from etiket.app.crud.db import (
    create_db_and_tables,
)
from etiket.core.init import (
        ensure_admin_user,
        check_storage_dirs,
        initialize_secure_file_flow,
        )
from etiket.core.docs import description, title, tags_metadata
from etiket.api.v1.router import router

app = FastAPI(title=title, description=description, openapi_tags=tags_metadata)
app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    ensure_admin_user()
    check_storage_dirs()
    initialize_secure_file_flow()
