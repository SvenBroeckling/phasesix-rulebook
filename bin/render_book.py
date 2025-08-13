import argparse
import os

import yaml


def main(args):
    source_file = args.source_file[0]
    book_root_directory = os.path.dirname(os.path.abspath(source_file[0]))
    book_yaml = load_book_yaml(source_file)
    print(args)
    print(book_yaml)


def load_book_yaml(source_file):
    with open(source_file) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source_file", help="Path to the source file", type=str, nargs=1
    )
    parser.add_argument(
        "--define",
        "-d",
        help="Define variables, i.E. -d key=value key2=value2",
        type=str,
        nargs="*",
    )
    main(parser.parse_args())
