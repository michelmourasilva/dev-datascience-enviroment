# -*- conding: UTF-8 -*-
import logging
import warnings

# Bibliotecas dos servidores - gunicorn
import multiprocessing
from gunicorn.app.base import BaseApplication
# Bibliotecas dos servidores - unicorn
import uvicorn

# Bibliotecas para o FastAPI
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse

from fastapi.responses import PlainTextResponse

# configuracoes
from core.api import get_api_settings

# bibliotecas internas
from src.env import APM_SERVICE_URL, APM_SERVICE_NAME, ENVIROMENT, NOME_API, DATABASE_SCHEMA, SERVER_WORKER, SERVER_LOG, SERVER_TIMEOUT

# bibliotecas referente ao banco de dados
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

# api - rotas
from controller import cadastro


get_api_settings.cache_clear()
settings = get_api_settings()

app = FastAPI(**settings.fastapi_kwargs)

# Configuraçào do CORS
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# Executa se o serviço de APM foi informado nas variáveis de ambiente
if APM_SERVICE_NAME != '':
    apm_config = {
        "SERVICE_NAME": APM_SERVICE_NAME,
        "SERVER_URL": APM_SERVICE_URL,
        "ENVIROMENT": ENVIROMENT,
        "ENABLED": True,
        "LOG_LEVEL": "trace",
        "LOG_FILE_SIZE": "200mb"}
    elasticapm = make_apm_client(apm_config)

    # inicializa o agente
    app.add_middleware(ElasticAPM, client=elasticapm)


@app.on_event("startup")
async def startup_event():
    print('Start')


@app.on_event("shutdown")
async def shutdown_event():
    print('Shutdown')


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):

    if exc.status_code == 404:
        retorno = 'Não encontrado'
    else:
        retorno = str(exc.detail)

    return PlainTextResponse(retorno, status_code=exc.status_code)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=422)


def configure_routing():
    app.include_router(cadastro.router, tags=["Consulta de condutores"])


# Modulos referentes ao gunicon
def number_of_workers():
    workers = SERVER_WORKER
    if workers in (0, ''):
        workers = (multiprocessing.cpu_count() * 2) + 1

    return workers


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def uvicorn_runner(host, port):
    uvicorn.run(app, host=host, port=port)

def gunicorn_runner(host, port):

    log = 'info' if SERVER_LOG in (None, '') else SERVER_LOG
    timeout = 30 if SERVER_TIMEOUT in (None, '') else SERVER_TIMEOUT

    options = {
        'bind': '%s:%s' % (host, port),
        'reload': True,
        'workers': number_of_workers(),
        'worker_class': 'uvicorn.workers.UvicornWorker',
        'accesslog': '-',
        'errorlog': '-',
        'loglevel': log,
    }

    StandaloneApplication(app, options).run()


if __name__ == '__main__':

    configure_routing()

    HOST = '0.0.0.0'
    PORT = 8000

    try:

        if ENVIROMENT == 'PRD':
            server_runner = gunicorn_runner
        else:
            server_runner = uvicorn_runner
    except Exception as err:
        server_runner = uvicorn_runner

    server_runner(HOST, PORT)
