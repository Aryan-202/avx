from moviepy.editor import AudioFileClip

def convert_ogg_to_flac(input_file: str, output_file: str) -> None:
    """Converts a ogg file to a flac file."""
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, logger=None)
    clip.close()
