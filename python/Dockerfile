FROM rust:1.50 as builder
WORKDIR /app
COPY silang .
RUN cargo install --path .


FROM python:3.9
WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv && \
    pipenv install --system
COPY . .
COPY --from=builder /usr/local/cargo/bin/silang /silang

CMD gunicorn -c gunicorn.py server:app
