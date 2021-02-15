FROM rust:1.50 as builder
WORKDIR /app
RUN git clone -b rust https://github.com/cordx56/silang.git /silang && \
    cd /silang && \
    cargo install --path .


FROM python:3.9
WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv && \
    pipenv install --system
COPY . .
COPY --from=builder /usr/local/cargo/bin/silang /silang

CMD gunicorn -c gunicorn.py server:app
