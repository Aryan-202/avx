import os
from rich.console import Console
from avx import converters

console = Console()

# Domain Definitions
DOMAINS = {
    "document": {".docx", ".pdf", ".txt", ".md", ".html", ".odt", ".pptx"},
    "image": {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff", ".gif"},
    "audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".webm"},
    "data": {".csv", ".json", ".xml", ".xlsx"},
    "archive": {".zip", ".tar", ".gz"}
}

def get_converter_func(input_ext: str, output_ext: str):
    """Get the converter function for the given extensions.

    Args:
        input_ext (str): The input extension.
        output_ext (str): The output extension.

    Returns:
        Callable: The converter function.
    """
    in_clean = input_ext.lstrip('.')
    out_clean = output_ext.lstrip('.')
    func_name = f"convert_{in_clean}_to_{out_clean}"
    
    return getattr(converters, func_name, None)



def get_domain(ext: str) -> str | None:
    """Get the domain for a given extension.

    Args:
        ext (str): The file extension.

    Returns:
        str | None: The domain name or None if unsupported.
    """
    for domain, exts in DOMAINS.items():
        if ext in exts:
            return domain
    return None

import glob

def predict_output_ext(input_ext: str) -> str:
    """Predict the logical output extension for an input extension.

    Args:
        input_ext (str): The input extension.

    Returns:
        str: The predicted output extension.
    """
    predictions = {
        ".docx": ".pdf", ".md": ".html", ".csv": ".json",
        ".png": ".jpg", ".jpg": ".png", ".jpeg": ".png",
        ".mp3": ".wav", ".wav": ".mp3",
        ".mp4": ".mkv", ".mkv": ".mp4"
    }
    return predictions.get(input_ext, ".out")

def process_single_file(input_file: str, output_file: str) -> None:
    """Process a single file conversion.

    Args:
        input_file (str): The input file path.
        output_file (str): The output file path.
    """
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if not input_ext or not output_ext:
        console.print(f"[bold red]Error:[/] Could not determine file extensions for {input_file}.")
        return

    in_domain = get_domain(input_ext)
    out_domain = get_domain(output_ext)

    if not in_domain or not out_domain:
        console.print(f"[bold red]Error:[/] Unsupported extensions '{input_ext}' -> '{output_ext}'.")
        return

    if in_domain != out_domain:
        console.print(f"[bold red]Cross-Domain Error:[/] Cannot convert {in_domain} to {out_domain}.")
        return

    converter_func = get_converter_func(input_ext, output_ext)

    if converter_func:
        try:
            converter_func(input_file, output_file)
            console.print(f"[bold green]Success:[/] Converted '{input_file}' to '{output_file}'.")
        except Exception as e:
            console.print(f"[bold red]Conversion Failed for '{input_file}':[/] {str(e)}")
    else:
        console.print(f"[bold yellow]Not Implemented:[/] '{input_ext}' to '{output_ext}'.")


def convert_files(input_pattern: str, output: str | None = None) -> None:
    """Convert files with batch and auto-output capabilities.

    Args:
        input_pattern (str): The input file path or wildcard.
        output (str, optional): The output file path, extension, or directory.
    """
    files = glob.glob(input_pattern)
    if not files:
        console.print(f"[bold red]Error:[/] No files found matching '{input_pattern}'.")
        return

    for input_file in files:
        if not os.path.isfile(input_file):
            continue
            
        if not output:
            # Auto-predict
            input_ext = os.path.splitext(input_file)[1].lower()
            out_ext = predict_output_ext(input_ext)
            output_file = os.path.splitext(input_file)[0] + out_ext
        elif output.startswith('.'):
            # It's an extension
            output_file = os.path.splitext(input_file)[0] + output
        elif os.path.isdir(output):
            # It's a directory
            input_ext = os.path.splitext(input_file)[1].lower()
            out_ext = predict_output_ext(input_ext)
            base_name = os.path.basename(os.path.splitext(input_file)[0])
            output_file = os.path.join(output, base_name + out_ext)
        else:
            # Explicit file
            if len(files) > 1:
                console.print("[bold red]Error:[/] Cannot output multiple files to a single file name.")
                return
            output_file = output

        process_single_file(input_file, output_file)
