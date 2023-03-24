import openai
from tqdm import tqdm
from typing import List
import io

# TODO: Modularize this into a class -> keep it consistent with other nns
def transcribe_audio_chunk(audio_chunk: io.BytesIO) -> str:
    audio_chunk.seek(0)
    txt = openai.Audio.transcribe('whisper-1', audio_chunk)
    transcription = txt['text'].strip()
    return transcription

def transcribe_audio_chunks(audio_chunks: List[io.BytesIO]) -> str:
    transcriptions = []
    
    for audio_chunk in tqdm(audio_chunks, desc="Transcribing audio chunks", unit="chunk"):
        transcription = transcribe_audio_chunk(audio_chunk)
        transcriptions.append(transcription)

    # Concatenate transcriptions
    full_transcription = "\n".join(transcriptions)
    return full_transcription