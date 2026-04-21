import argparse
from avx.commands import ls

def main():
    parser = argparse.ArgumentParser(description="avx CLI")

    subparsers = parser.add_subparsers(dest="command")

    ls_parser = subparsers.add_parser("ls", help="list files")
    ls_parser.add_argument("-a", "--all", action="store_true")

    args = parser.parse_args()

    if args.command == "ls":
        ls.list_files(args)
    else:
        parser.print_help()