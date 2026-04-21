import os

def run(args):
    files = os.listdir(".")

    for f in files:
        if not args.all and f.startswith("."):
            continue
        print(f)

        