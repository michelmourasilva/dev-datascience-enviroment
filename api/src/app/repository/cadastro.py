from sqlalchemy.orm import Session
from models.cadastro import CadastroDB
import repository.bloqueio as bloqueio
from sqlalchemy import func

# Linhas comentadas são referente a paginação dos dados
# def get_data(db: Session, cpf: str = None, numeroRegistroCnh: int = None, formularioRenach: str = None, page: int = 1, limit: int = 100):
def get_data(db: Session, cpf: str = None, numeroRegistroCnh: int = None, formularioRenach: str = None, pgu: str = None):
    """
    Recupera dados dos cadastros e bloqueios de um condutor
    """
    filtro = {'situacaoExclusaoCondutor': ''}
    if cpf:
        filtro.update({'cpf': cpf})
    if numeroRegistroCnh:
        filtro.update({'_numeroFormularioCnh': numeroRegistroCnh})
    if formularioRenach:
        filtro.update({'numeroFormularioRenach': formularioRenach})
    if pgu:
        filtro.update({'_numeroPgu': pgu})

    resultado = db.query(CadastroDB, func.count().over().label('total'), func.max(CadastroDB.cpf).over().label('idUltimoRegistro')).filter_by(**filtro).order_by(CadastroDB.cpf.asc()).all()
    # resultado = db.query(CadastroDB, func.count().over().label('total'), func.max(CadastroDB.cpf).over().label('idUltimoRegistro')).filter_by(**filtro).order_by(CadastroDB.cpf.asc()).offset((page * limit) - limit).limit(limit).all()

    condutores = [i[0] for i in resultado]
    quantidaderegistros = len(condutores)
    if quantidaderegistros > 0:
        quantidadeReal = resultado[0][1]
        # Comentado pois não foi identificado qual a chave a ser apresentada, portanto para atender a subistituição da APi do Denatran será retornado o valor zerao
        # ultimoRegistro = resultado[0][2]
        ultimoRegistro = 0
    else:
        condutores = []
        quantidadeReal = 0
        ultimoRegistro = 0

    retorno = {'quantidade': len(condutores), 'quantidadeReal': quantidadeReal, 'idUltimoRegistro': ultimoRegistro, 'condutor': condutores}
    
    return retorno
