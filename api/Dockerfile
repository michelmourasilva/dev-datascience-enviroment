# imagem oficial
FROM python:3.8.1-alpine

# diretório de trabalho
WORKDIR /usr/src/app

# Informar as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copia os requerimentos específicos para a API
COPY src/requirements.txt /usr/src/app/requirements.txt

# instala as dependências
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copia os arquivos do projeto
COPY src /usr/src/app/

EXPOSE 5432