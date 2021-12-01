from pydantic import BaseModel
import inspect
import datetime

def optional_validator(*fields):
    def dec(_cls):
        for field in fields:
            _cls.__fields__[field].required = False
        return _cls

    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], BaseModel):
        cls = fields[0]
        fields = cls.__fields__
        return dec(cls)
    return dec


def getniveisdicionario(dicionario, nivel=1):
    if not isinstance(dicionario, dict) or not dicionario:
        return nivel
    return max(getniveisdicionario(dicionario[key], nivel + 1)
               for key in dicionario)

def repetefuncao(funcao, n, valor):
    for i in range(n):
        valor = funcao(valor)
    return valor

def removenulosdicionario(dicionario):
    lista_exclude = []

    if type(dicionario) is dict:
        _temp = {}
        for k, v in dicionario.items():
            if v is None or v == "" or v.strftime('%Y-%m-%d') == '0001-01-01':
                lista_exclude.append(k)
 
    retorno = lista_exclude
    return retorno

def validacpf(cpf, d1=0, d2=0, i=0):
    retorno = False

    if cpf is not None:
        if cpf.isdecimal() is True:
            while i < 10:
                d1, d2, i = (d1 + (int(cpf[i]) * (11 - i - 1))) % 11 if i < 9 else d1, (d2 + (int(cpf[i]) * (11 - i))) % 11, i + 1
            retorno = (int(cpf[9]) == (11 - d1 if d1 > 1 else 0)) and (int(cpf[10]) == (11 - d2 if d2 > 1 else 0))
    return retorno

def retorno_data(_data):
    return None if _data.strftime('%Y-%m-%d') == '0001-01-01' else _data
