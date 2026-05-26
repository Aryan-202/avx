import typer
from avx.commands.ls import list_files
from avx.commands.convert import convert_files

app = typer.Typer(help="avx CLI - A powerful file conversion tool")

@app.command(name="ls")
def ls_cmd(all: bool = typer.Option(False, "--all", "-a", help="Include hidden files")):
    """List files and directories in the current working directory."""
    list_files(all)

@app.command(name="convert")
def convert_cmd(
    input: str = typer.Argument(..., help="Input file path or wildcard (e.g., *.png)"),
    output: str = typer.Option(None, "--output", "-o", help="Output file path, extension, or directory")
):
    """Convert a file from one format to another."""
    convert_files(input, output)

def main():
    """Main entry point for the avx CLI."""
    app()

if __name__ == "__main__":
    main()