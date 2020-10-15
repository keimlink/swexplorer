# Star Wars Character Explorer

Demonstrative project to browse characters fetched from [SWAPI](https://github.com/phalt/swapi).

## Prerequisites

- [Python](https://www.python.org/) >= 3.8 (automatically installed if [pyenv](https://github.com/pyenv/pyenv) is available)
- [Poetry](https://python-poetry.org/)

## Installation

To bootstrap the project run:

```console
./scripts/bootstrap.sh
```

Now activate the virtual environment:

```console
poetry shell
```

After that apply the migrations:

```console
./manage.py migrate
```

## Usage

Start the development web server (with the virtual environment activated):

```console
./manage.py runserver
```

Now open `http://127.0.0.1:8000/` in your browser to use the application.
