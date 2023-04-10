import logging

log = logging.getLogger("lore_vectorizer")
logging.basicConfig(level=logging.INFO)

import argparse
import os
from pathlib import Path
from typing import List

import joblib
import numpy as np
from nltk.corpus import stopwords
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

# all English stop words
stop_words = list(set(stopwords.words("english")))


def get_args() -> argparse.Namespace:
    """
    Get the command line arguments via argparse.
    """

    parser = argparse.ArgumentParser(
        prog="lore_vectorizer", description="Vectorize lore via TF-IDF"
    )
    parser.add_argument(
        "lore_dir",
        help="The directory containing all lore documents.",
        default="../.data/lore/",
        nargs="?",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        help="The directory to output vectorizer pipeline to.",
        default="../.data/vectorizer/",
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    """
    Validate the command line arguments.
    """

    # validate lore directory
    if not args.lore_dir:
        raise ValueError("Lore directory must be specified")
    if not os.path.exists(args.lore_dir):
        raise ValueError("Lore directory does not exist")
    if not os.path.isdir(args.lore_dir):
        raise ValueError("Lore directory is not a directory")
    # validate output directory
    if not args.output_dir:
        raise ValueError("Output directory must be specified")
    if not os.path.exists(args.output_dir):
        raise ValueError("Output directory does not exist")
    if not os.path.isdir(args.output_dir):
        raise ValueError("Output directory is not a directory")

    return {
        "lore_dir": Path(args.lore_dir),
        "output_dir": Path(args.output_dir),
    }


def get_all_lore_files(lore_dir: Path) -> List[Path]:
    """
    Get all lore files from the given directory.
    """
    return list(lore_dir.glob("*.txt"))


def create_pipeline() -> Pipeline:
    global stop_words
    vectorizer = TfidfVectorizer(stop_words=stop_words, max_df=0.10, ngram_range=(1, 3))
    svd = TruncatedSVD(n_components=1000)
    pipeline = Pipeline([("vectorizer", vectorizer), ("svd", svd)])
    return pipeline


def main():
    args = validate_args(get_args())

    # read all lore files
    lore_paths = get_all_lore_files(args["lore_dir"])
    log.info(f"Reading all lore files from {args['lore_dir'].resolve()}")
    all_lore = {lore_path.stem: lore_path.read_text() for lore_path in lore_paths}

    # create pipeline and fit, transform all lore docs to vectors
    log.info(f"Fitting and transforming all {len(all_lore)} lore docs to vectors")
    pipeline = create_pipeline()
    doc_vectors = pipeline.fit_transform(all_lore.values())
    log.info("Transform complete.")

    # print out explained variance ratio
    log.info(
        f"Explained variance ratio sum: {pipeline['svd'].explained_variance_ratio_.sum()}"
    )

    # save doc vectors
    log.info("Saving doc vectors")
    np.save(args["output_dir"] / "doc_vectors.npy", doc_vectors)

    # save pipeline
    log.info("Saving vector pipeline")
    joblib.dump(pipeline, args["output_dir"] / "vector_pipeline.joblib.gz")

    # save doc name order
    log.info("Saving doc names")
    np.save(args["output_dir"] / "doc_names.npy", np.array(list(all_lore.keys())))


if __name__ == "__main__":
    main()
