from moviepy.editor import AudioFileClip

def convert_aac_to_ogg(input_file: str, output_file: str) -> None:
    """Converts a aac file to a ogg file."""
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, logger=None)
    clip.close()
