import os
import comtypes.client

def convert_pptx_to_pdf(input_path: str, output_path: str) -> None:
    """
    Converts a PPTX file to a PDF using Microsoft PowerPoint COM interop.
    
    Args:
        input_path: Path to the source .pptx file.
        output_path: Path where the .pdf should be saved.
    """
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1  

    deck = powerpoint.Presentations.Open(os.path.abspath(input_path))

    deck.SaveAs(os.path.abspath(output_path), 32)

    deck.Close()
    powerpoint.Quit()
