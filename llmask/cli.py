import argparse

def cli_entrypoint():
    parser = argparse.ArgumentParser(description="My CLI tool.")
    parser.add_argument("name", help="Your name.")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")