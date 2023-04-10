import argparse
import os

from data_service.database.connection import get_db
from data_service.database.lore_store import ChampLore


def get_args() -> argparse.Namespace:
    """
    Get the command line arguments via argparse.
    """

    parser = argparse.ArgumentParser(
        prog="lore_downloader", description="Lore downloader script from Voidling DB"
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        help="The directory to output all lore docs to.",
        required=True,
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    """
    Validate the command line arguments.
    """

    if not args.output_dir:
        raise ValueError("Output directory must be specified")
    if not os.path.exists(args.output_dir):
        raise ValueError("Output directory does not exist")
    if not os.path.isdir(args.output_dir):
        raise ValueError("Output directory is not a directory")


def main():
    args = get_args()
    validate_args(args)
    db = get_db()
    for doc in db["lore"].find():
        validated_doc = ChampLore(**doc)
        with open(os.path.join(args.output_dir, f"{validated_doc.id}.txt"), "w") as f:
            to_write = f"{validated_doc.name}\n\n{validated_doc.lore}"
            f.write(to_write)


if __name__ == "__main__":
    main()
