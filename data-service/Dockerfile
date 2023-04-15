# syntax=docker/dockerfile:1
FROM python:3.10-bullseye

# parameters
ARG RIOT_API_KEY
ARG DDRAGON_ROOT_URL=https://ddragon.leagueoflegends.com/cdn/13.6.1/data/en_US
ARG DB_NAME=voidlingdata
ARG DB_URL

# set environment variables
ENV RIOT_API_KEY=$RIOT_API_KEY
ENV DDRAGON_ROOT_URL=$DDRAGON_ROOT_URL
ENV DB_NAME=$DB_NAME
ENV DB_URL=$DB_URL
ENV VECTORIZER_PATH=/app/trained_vectorizer/vector_pipeline.joblib.gz
ENV DOC_VECTORS_PATH=/app/trained_vectorizer/doc_vectors.npy
ENV DOC_NAMES_PATH=/app/trained_vectorizer/doc_names.npy

# poetry install
ENV POETRY_VERSION 1.4.0
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/root/.local/bin:/opt/venv/bin:${PATH}"

# install dependencies
RUN mkdir -p /app
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN poetry install --no-dev --no-root --no-interaction

# copy over hugging face stuff
RUN poetry run python -c "from transformers import pipeline; pipeline('question-answering', model='distilbert-base-cased-distilled-squad'); pipeline('summarization', model='yasminesarraj/flan-t5-small-samsum')"

# install nltk stuff
RUN poetry run python -m nltk.downloader stopwords

# copy over source code
COPY . /app
EXPOSE 8000
CMD ["poetry", "run", "sanic", "data_service.server:app", "-p", "8000", "--host=0.0.0.0"]
