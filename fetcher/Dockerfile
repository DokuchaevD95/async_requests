FROM python:3.10.3-alpine3.15

ARG APP_PATH=/opt/fetcher

WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    rm requirements.txt

RUN mkdir -p $APP_PATH
COPY src/ $APP_PATH/

WORKDIR $APP_PATH

EXPOSE 8000
