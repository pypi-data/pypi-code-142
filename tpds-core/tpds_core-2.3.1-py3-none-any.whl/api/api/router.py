from fastapi import APIRouter

from .hw import api_board, api_device
from .manifest_file import api_manifest

api_router = APIRouter()
api_router.include_router(api_board.router, prefix="/boards", tags=["Boards"])
api_router.include_router(api_device.router, prefix="/device", tags=["Device"])
api_router.include_router(api_manifest.router, prefix="/manifest", tags=["Manifest"])
