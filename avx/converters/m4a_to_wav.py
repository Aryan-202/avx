from moviepy.editor import AudioFileClip

def convert_m4a_to_wav(input_file: str, output_file: str) -> None:
    """Converts a m4a file to a wav file."""
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, logger=None)
    clip.close()
