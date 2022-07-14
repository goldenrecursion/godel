FROM nvidia/cuda:11.0-devel-ubuntu20.04 as base

# Set lang
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Set python env vars
ENV PYTHONUNBUFFERED=1 \
    # Prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # Pip
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    \
    # Poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.1.11 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/opt/.venv"

ENV PATH="/opt/poetry/bin:$VENV_PATH/bin:$PATH"

# Install python 3.9
ENV DEBIAN_FRONTEND=noninteractive

# Rotating Keys
RUN rm /etc/apt/sources.list.d/cuda.list

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common \
    git \
    git-lfs \
    ssh \
    python3.9 \
    python3.9-dev \
    python3.9-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
WORKDIR /opt
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3.9 -
RUN python3.9 -m pip install --upgrade pip

# install poetry dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install && \
    poetry install -E "web3 data-tools docs"

# Copy source code to the image
COPY . ./godel
ENV PYTHONPATH=/opt/godel/src:$PYTHONPATH

from base as test
RUN pytest