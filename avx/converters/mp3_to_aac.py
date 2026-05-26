from moviepy.editor import AudioFileClip

def convert_mp3_to_aac(input_file: str, output_file: str) -> None:
    """Converts a mp3 file to a aac file."""
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, logger=None)
    clip.close()
