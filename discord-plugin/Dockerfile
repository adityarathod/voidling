# syntax=docker/dockerfile:1
FROM python:3.10-bullseye

# parameters
ARG DISCORD_TOKEN
ARG RASA_SERVER_URL=http://bot-core:5005
ARG BOT_PREFIX=

# set environment variables
ENV DISCORD_TOKEN=$DISCORD_TOKEN
ENV RASA_SERVER_URL=$RASA_SERVER_URL
ENV BOT_PREFIX=$BOT_PREFIX

# poetry install
ENV POETRY_VERSION 1.4.0
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/root/.local/bin:/opt/venv/bin:${PATH}"

# install dependencies
RUN mkdir -p /app
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN poetry install --no-dev --no-root --no-interaction

# copy over source code
COPY . /app
CMD ["poetry", "run", "python", "-m", "voidling_discord"]
