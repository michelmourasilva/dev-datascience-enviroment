from fastapi import APIRouter, Depends, HTTPException, status, Path, Query, Response
from schemas.cadastro import CadastroBaseSchema, CondutorBase
from repository.cadastro import get_data
from sqlalchemy.orm import Session
from typing import List, Optional
from core.database import SessionLocal
from src.env import DATABASE_URL
from core.util import validacpf, removenulosdicionario
from fastapi.responses import JSONResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def descricao_base(**kwargs):

    descricao_base = ('Recupera dados de condutores e ocorrências',)
    filtros = kwargs.get('filtros', [])

    if 'cpf' in filtros:
        descricao_base += (' por cpf',)

    if 'numeroRegistroCnh' in filtros:
        descricao_base += (' e por número do registro CNH',)

    if 'formularioRenach' in filtros:
        descricao_base += (' por formulário Renach',)

    if 'pgu' in filtros:
        descricao_base += (' por Prontuário Geral Unificado (PGU)', )

    if 'numeroRegistroCnh' in filtros:
        descricao_base += (' por número de registro da CNH', )

    retorno = ''.join(descricao_base)

    return retorno


# @router.get("/condutores/", response_model=CondutorBase, name=descricao_base())
@router.get("/condutores/cpf/{cpf}/", response_model=CondutorBase, name=descricao_base(filtros=['cpf']), response_model_exclude_none=True, response_model_exclude_unset=True)
@router.get("/condutores/cpf/{cpf}/registroCnh/{numeroRegistroCnh}", response_model=CondutorBase, name=descricao_base(filtros=['cpf', 'numeroRegistroCnh']), response_model_exclude_unset=True)
@router.get("/condutores/formularioRenach/{formularioRenach}", response_model=CondutorBase, name=descricao_base(filtros=['formularioRenach']), response_model_exclude_unset=True)
@router.get("/condutores/pgu/{pgu}", response_model=CondutorBase, name=descricao_base(filtros=['pgu']), response_model_exclude_unset=True)
@router.get("/condutores/registroCnh/{numeroRegistroCnh}", response_model=CondutorBase, name=descricao_base(filtros=['numeroRegistroCnh']), response_model_exclude_unset=True)
async def get_data_cadastro(response: Response,
                            cpf: str = None,
                            numeroRegistroCnh: str = None,
                            formularioRenach: str = None,
                            pgu: str = None,
                            db: Session = Depends(get_db)
                            # page: Optional[int] = Query(1, description="Valor igual ou acima de 1", ge=1),
                            # limit: Optional[int] = Query(100, description="Valor entre 1 e 100", ge=1, le=100)
                            ):
    """
    Retorna dados de condutores e ocorrências
    """
    try:
        # Validação do CPF

        if validacpf(cpf) is False and cpf is not None:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'returnCode': 1, 'message': 'CPF inválido'})
        else:

            # comentando a paginação
            # resultado = get_data(db, cpf, numeroRegistroCnh, formularioRenach, page, limit)
            resultado = get_data(db, cpf, numeroRegistroCnh, formularioRenach, pgu )
            
            if resultado['quantidade'] > 0:
                response.status_code = status.HTTP_200_OK
                response.response_model = CondutorBase
                # response.response_model_exclude = lista_exclusao
                return resultado

            else:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'returnCode': 1, 'message': 'Condutor não encontrado'})

    except Exception as err:

        print('Erro ao apresentar os dados', err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            # Comentado para dar lugar a mensagem da API WSDENATRAN
            # detail=f"Não foi possível recuperar corretamente os dados. Por favor verifique o log da aplição.",)
            detail=f"FALHA_INTERNA",)
