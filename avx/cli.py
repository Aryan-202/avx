import argparse
from avx.commands import list_files, convert_files

def main():
    """
    Main entry point for the avx CLI.

    Parses command-line arguments and routes to the appropriate command handler.
    """
    parser = argparse.ArgumentParser(description="avx CLI")

    subparsers = parser.add_subparsers(dest="command")

    ls_parser = subparsers.add_parser("ls", help="list files")
    ls_parser.add_argument("-a", "--all", action="store_true")

    convert_parser = subparsers.add_parser("convert", help="convert files")
    convert_parser.add_argument("input", help="input file path")
    convert_parser.add_argument("-o","--output", required=True, help="output file path")

    args = parser.parse_args()

    if args.command == "ls":
        list_files(args)
    elif args.command == "convert":
        convert_files(args)
    else:
        parser.print_help()