from functools import lru_cache
from typing import Any, Dict

from pydantic import BaseSettings


class APISettings(BaseSettings):
    """
    Classe que permite a configuração de instância FastAPI por meio do uso de variáveis ​​de ambiente.
    Qualquer um dos atributos da instância pode ser substituído na instanciação, passando o valor desejado para o
    inicializador ou definindo a variável de ambiente correspondente.
    """

    # fastapi.applications.FastAPI initializer kwargs
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "API"
    version: str = "0.0.1"

    # Custom settings
    disable_docs: bool = False

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """
        Retorna um dicionário dos argumentos de palavra-chave mais usados ​​ao inicializar uma instância FastAPI
        Se 'self.disable_docs' for True, os vários argumentos relacionados ao docs são desabilitados, evitando que sua especificação seja
        publicada.
        """
        fastapi_kwargs: Dict[str, Any] = {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
        if self.disable_docs:
            fastapi_kwargs.update({"docs_url": None, "openapi_url": None, "redoc_url": None})
        return fastapi_kwargs

    class Config:
        env_prefix = "api_"
        validate_assignment = True


@lru_cache()
def get_api_settings() -> APISettings:
    """
    Função que retorna uma instância em cache do objeto APISettings.
    O cache é usado para evitar a releitura do ambiente toda vez que as configurações da API são usadas em um terminal.
    Se for preciso alterar uma variável de ambiente e redefinir o cache (por exemplo, durante o teste), isso pode ser feito
    usando o método de instância 'lru_cache get_api_settings.cache_clear ()'.
    """
    return APISettings()
