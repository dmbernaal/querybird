from fastapi import APIRouter, File, UploadFile, Form
from starlette.responses import JSONResponse

from ..utils import split_audio

from ..nn.whisper import transcribe_audio_chunks
from ..nn.chatgpt import project_manager

router = APIRouter()

# @router.post("/", summary="upload audio to get the ticket")
# async def upload_audio(audio_file: UploadFile = File(...), audio_format: str = Form(...)):
#     # Process the audio file
#     audio_chunks = split_audio(audio_file.file, audio_format)

#     # Perform NLP logic -> get transcription
#     transcription = transcribe_audio_chunks(audio_chunks)

#     # Perform NLP logic -> get ticket
#     response = project_manager.get_ticket(transcription)

#     response = {"message": "success"}
#     return JSONResponse(
#         status_code=200,
#         content={
#             "response": response
#         }
#     )

@router.post("/audio", summary="upload audio to get the ticket")
async def upload_audio(recordings: UploadFile = File(...)):
    audio_format = "m4a"
    # Process the audio file
    print("Chunking audio...")
    audio_chunks = split_audio(recordings.file, audio_format)

    # Perform NLP logic -> get transcription
    print("Transcribing audio...")
    transcription = transcribe_audio_chunks(audio_chunks)

    # Perform NLP logic -> get ticket
    print("Generating ticket...")
    response = project_manager(transcription)

    print(f"Generated ticket: {response}")
    return JSONResponse(
        status_code=200,
        content={
            "response": {"ticket": response} 
        }
    )