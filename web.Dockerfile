FROM alpine
RUN apk add --update --no-cache python3
RUN apk add --update postgresql-dev gcc python3-dev musl-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools django psycopg2
COPY ./projeto /projeto