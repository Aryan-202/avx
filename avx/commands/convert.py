import os
from avx import converters

def convert_files(args: object) -> None:
    """
    Convert a file from one format to another based on its extension.

    Args:
        args (argparse.Namespace): Command-line arguments containing the input
            file path (args.input) and the output file path (args.output).
    """
    input_file: str = args.input
    output_file: str = args.output

    if not os.path.exists(input_file):
        print('file does not exists')
        return
    
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext == '.docx' and output_ext == '.pdf':
        converters.convert_docx_to_pdf(input_file, output_file)
    elif input_ext == '.pptx' and output_ext == '.pdf':
        converters.convert_pptx_to_pdf(input_path=input_file, output_path=output_file)
    else:
        print('conversion not supported')
