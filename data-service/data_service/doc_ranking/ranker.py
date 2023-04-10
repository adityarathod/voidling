import os
from typing import List

import numpy as np

DOC_VECTORS_PATH = os.getenv("DOC_VECTORS_PATH")
DOC_NAMES_PATH = os.getenv("DOC_NAMES_PATH")
doc_vectors: np.ndarray = np.load(DOC_VECTORS_PATH)
doc_names: np.ndarray = np.load(DOC_NAMES_PATH)


def rank_vector(vector: np.ndarray, top_n: int = 1) -> List[str]:
    """
    Rank a vector against the document vectors using cosine similarity.
    """
    similarity = np.dot(doc_vectors, vector) / (
        np.linalg.norm(doc_vectors, axis=1) * np.linalg.norm(vector)
    )
    all_names = doc_names[np.argsort(similarity)[-top_n:][::-1]]
    return all_names.tolist()
