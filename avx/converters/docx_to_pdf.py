from docx2pdf import convert


def convert_docx_to_pdf(input_file: str, output_file: str) -> None:
    """
    Converts a DOCX file to a PDF using docx2pdf.
    
    Args:
        input_file: Path to the source .docx file.
        output_file: Path where the .pdf should be saved.
    """
    convert(input_path= input_file, output_path= output_file)
    