import logging

log = logging.getLogger(__name__)

import os
import joblib
import numpy as np
from sklearn.pipeline import Pipeline

VECTORIZER_PIPELINE_PATH = os.getenv("VECTORIZER_PATH")
log.info(f"Loading vectorizer from {VECTORIZER_PIPELINE_PATH}")
vectorizer: Pipeline = joblib.load(VECTORIZER_PIPELINE_PATH)


def vectorize_query(query: str) -> np.ndarray:
    """
    Vectorize a query string.
    """
    return vectorizer.transform([query])[0]
