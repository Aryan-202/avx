from moviepy.editor import AudioFileClip

def convert_aac_to_mp3(input_file: str, output_file: str) -> None:
    """Converts a aac file to a mp3 file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, logger=None)
    clip.close()
