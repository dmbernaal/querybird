# router handling and middleware
from fastapi import APIRouter

from .upload_audio.view import router as upload_audio_router

# instantiate router
api_router = APIRouter()

# add routes to router
api_router.include_router(upload_audio_router, prefix="/upload", tags=["upload audio"])
