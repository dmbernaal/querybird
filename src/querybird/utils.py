# BASE UTILS. 
# TODO: These will be modularized into separate files and folders in the future.
import os
import pytube
import moviepy.editor as mp
from moviepy.editor import AudioFileClip
from pydub import AudioSegment
from tqdm.notebook import tqdm
import io

# VIDEO UTILS
# Download video from youtube
# TODO: modulate into class to download from various sources
def download_video(url, path, local=False):
    if local:
        return url
    else:
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_name = f"{yt.title}-{yt.video_id}.mp4"
        file_path = os.path.join(path, file_name)
        stream.download(output_path=path, filename=file_name)
        return file_name

# Convert video to audio
def video2audio(video_path, audio_path, audio_format="mp3"):
    audio = mp.AudioFileClip(video_path)
    audio.write_audiofile(audio_path, bitrate="192k", codec=audio_format)

# Process video, main wrapper function
def process_video(url, base_path, local=False, audio_format="mp3"):
    if not local:
        data_path = os.path.join(base_path, "data")
        os.makedirs(data_path, exist_ok=True)

    audio_path = os.path.join(base_path, "audio")
    chunks_path = os.path.join(base_path, "chunks")
 
    os.makedirs(audio_path, exist_ok=True)
    os.makedirs(chunks_path, exist_ok=True)

    # Download the video or use the local file
    video_file_name = download_video(url, data_path if not local else "", local)
    video_file_path = os.path.join(data_path if not local else "", video_file_name)

    # Convert the video to audio
    audio_file_name = f"{os.path.splitext(video_file_name)[0]}.{audio_format}"
    audio_file_path = os.path.join(audio_path, audio_file_name)
    video2audio(video_file_path, audio_file_path, audio_format)

    # Split the audio into chunks
    audio_chunks_path = os.path.join(chunks_path, os.path.splitext(video_file_name)[0])
    os.makedirs(audio_chunks_path, exist_ok=True)
    split_audio(audio_file_path, audio_chunks_path, audio_format=audio_format)

# AUDIO UTILS
_supported_formats_ = ["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]

class UnsupportedAudioFormatException(Exception):
    pass

class NamedBytesIO(io.BytesIO):
    def __init__(self, *args, **kwargs):
        self._name = kwargs.pop("name", "unknown")
        super(NamedBytesIO, self).__init__(*args, **kwargs)

    @property
    def name(self):
        return self._name

def split_audio(input_file, input_audio_format, output_audio_format="mp3", chunk_duration=60, min_duration_for_chunking=300):
    # Check if the audio format is supported
    if input_audio_format not in _supported_formats_:
        raise UnsupportedAudioFormatException("Unsupported audio format. Supported formats: mp3, mp4, mpeg, mpga, m4a, wav, webm")

    # Convert the input file to an AudioSegment object
    input_file.seek(0)
    audio = AudioSegment.from_file(input_file, format=input_audio_format)
    total_duration = audio.duration_seconds

    # If the audio duration is below the threshold, return the original audio file as a byte stream
    if total_duration < min_duration_for_chunking:
        audio_byte_stream = NamedBytesIO(name=f"audio.{output_audio_format}")
        audio.export(audio_byte_stream, format=output_audio_format)
        audio_byte_stream.seek(0)
        return [audio_byte_stream]

    audio_chunks = []
    for i in range(0, int(total_duration), chunk_duration):
        start_time = i * 1000
        end_time = (i + chunk_duration) * 1000 if i + chunk_duration < total_duration else total_duration * 1000
        audio_chunk = audio[start_time:end_time]
        
        # Export the audio chunk to a byte stream and add it to the list of audio_chunks
        audio_chunk_byte_stream = NamedBytesIO(name=f"audio_chunk_{i//chunk_duration}.{output_audio_format}")
        audio_chunk.export(audio_chunk_byte_stream, format=output_audio_format)
        audio_chunk_byte_stream.seek(0)
        audio_chunks.append(audio_chunk_byte_stream)

    return audio_chunks

