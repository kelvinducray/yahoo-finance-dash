ARG PYTHON_VERSION=3.10.3
FROM python:${PYTHON_VERSION}

ENV POETRY_VERSION 1.1.13

RUN pip3 install poetry==$POETRY_VERSION

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev --no-interaction --no-ansi

CMD poetry run yahoo_finance_dash