from argparse import ArgumentParser


def main():
    argparser = ArgumentParser()
    argparser.add_argument(
        "file",
        help="This is the file name to generate",
        type=str,
    )
    args = argparser.parse_args()
    with open(f"{args.file}.txt", "w") as f:
        f.write("Hello World!")


if __name__ == "__main__":
    main()
