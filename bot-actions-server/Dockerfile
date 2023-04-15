# syntax=docker/dockerfile:1
FROM python:3.10-bullseye

# parameters
ARG DATA_SERVICE_PORT=8000
ARG DATA_SERVICE_HOST=data-service

# set environment variables
ENV DATA_SERVICE_URL=http://${DATA_SERVICE_HOST}:${DATA_SERVICE_PORT}

# poetry install
ENV POETRY_VERSION 1.4.0
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/root/.local/bin:/opt/venv/bin:${PATH}"

# install dependencies
RUN mkdir -p /app
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN poetry install --no-dev --no-root --no-interaction


COPY . /app
EXPOSE 5055
CMD ["poetry", "run", "python", "-m", "rasa_sdk", "--actions", "voidling_actions"]
