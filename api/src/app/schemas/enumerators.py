from enum import Enum


class Enum_EstadosBr(str, Enum):
    AC = "AC"
    AL = "AL"
    AP = "AP"
    AM = "AM"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MT = "MT"
    MS = "MS"
    MG = "MG"
    PA = "PA"
    PB = "PB"
    PR = "PR"
    PE = "PE"
    PI = "PI"
    RJ = "RJ"
    RN = "RN"
    RS = "RS"
    RO = "RO"
    RR = "RR"
    SC = "SC"
    SP = "SP"
    SE = "SE"
    TO = "TO"


class Enum_permissionario(int, Enum):
    SIM = 1
    NAO = 2
    NOVA_PERMISSAO = 3

class Enum_sexo(int, Enum):
    INEXISTENTE = 0
    MASCULINO = 1
    FEMININO = 2

class Enum_nacionalidade(int, Enum):
    BRASILEIRO = 1
    BRASILEIRO_NATURALIZADO = 2
    ESTRANGEIRO = 3
    BRASILEIRO_NASCIDO_EXTERIOR = 4
