from sqlalchemy.orm import Session
from models.bloqueio import BloqueioDB

def get_data(db: Session, cpf: str):
    """
    Recupera dados de bloqueios de um condutor
    """
    filtro = {}

    if cpf:
        filtro.update({'cpf': cpf})

    retorno = db.query(BloqueioDB).filter_by(**filtro).all()
    # retorno = db.query(t_tb_cadastro_renach).all()
    return retorno
