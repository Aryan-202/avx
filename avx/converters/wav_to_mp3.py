from moviepy.editor import AudioFileClip

def convert_wav_to_mp3(input_file: str, output_file: str) -> None:
    """Converts a wav file to a mp3 file."""
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, logger=None)
    clip.close()
