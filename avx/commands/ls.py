import os
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

def list_files(args):
    files = os.listdir(".")

    table = Table(title="Current Working Directory")

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Type", style="magenta")
    table.add_column("Size (bytes)", justify="right", style="green")
    table.add_column("Modified", style="yellow")

    for f in files:
        if not args.all and f.startswith("."):
            continue

        path = os.path.join(".", f)

        file_type = "Dir" if os.path.isdir(path) else "File"
        size = str(os.path.getsize(path)) if os.path.isfile(path) else "-"
        modified = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")

        table.add_row(f, file_type, size, modified)

    console.print(table)