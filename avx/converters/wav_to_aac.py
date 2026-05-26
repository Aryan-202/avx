from moviepy.editor import AudioFileClip

def convert_wav_to_aac(input_file: str, output_file: str) -> None:
    """Converts a wav file to a aac file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, logger=None)
    clip.close()
