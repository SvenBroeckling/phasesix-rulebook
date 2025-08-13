import argparse


def main(args):
    print(args)


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
    args = parser.parse_args()
    main(args)
