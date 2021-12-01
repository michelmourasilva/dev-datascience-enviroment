from typing import Optional, Any
from pydantic import BaseModel, validator, Field
import datetime
from core.util import optional_validator

@optional_validator('ufDetranBloqueio', 'descricaoPrazoBloqueio')
class BloqueioBaseSchema(BaseModel):

#    NU_CONTROLE_CONDUTOR: int = Field(description='Numero de Controle dos Condutores. Identifica de forma única o Condutor, evitando redundancias encontradas no Cadastro Nacional de Pessoa Fisica - CPF')
#    cpf: str = Field(description='Numero do Cadastro de Pessoa Fisica - CPF, do Candidato ou Condutor')
    ufDetranBloqueio: str = Field(description='Departamento de Transito responsavel pelo registro do bloqueio ')
    dataImpedimentoBloqueio: Any = Field(description='Data do bloqueio / impedimento')
    motivoImpedimentoBloqueio: str = Field(description='Motivo do impedimento do Cidadão:  0, 1, 4, 7    Motivo do Bloqueio do candidato/condutor:  1, 2, 3, 4, 5, 8, 9, A, D, E, F')
    descricaoMotivoImpedimentoBloqueio: str = Field(description='Motivo do impedimento do Cidadão:  0 – Medida Administrativa (somente para o DENATRAN)  1 – IMPEDIDO DE SER HABILITADO  4 – MORTE   7 – INAPTO Motivo do Bloqueio do candidato/condutor:  1 – Impedido de ser Habilitado (292 a 294).  2 – Suspensão do Direito de Dirigir (261 e Resolução 182).  3 – Cassação CNH (Artigo 263 e Resolução 182).  4 – Morte.  5 – Cancelamento de Cadastro por Irregularidade (263 Paragrafo 1º).  8 – Permissionário Penalizado (Artigo 148 Parágrafos 3º e 4º).  9 – Habilitação Cancelada por Emissão Indevida  A – Permissionário Penalizado Após a Expedição da CNH (Artigo 148 Parágrafos 3º e 4º)  D – Medida Administrativa  E – Delito de Trânsito – Resolução 300  F – Acidente Grave – Resolução 300')
    orgaoResponsavelImpedimentoBloqueio: int = Field(description='Código que identifica o órgão responsavel pelo impedimento.')
    documentoGeradorImpedimentoBloqueio: str = Field(description='Descrição de identificação do documento que gerou o bloqueio ou impedimento')
    dataInicioImpedimentoBloqueio: Any = Field(description='Data de inicio da penalidade aplicada')
    dataTerminoImpedimentoBloqueio: Any = Field(description='Data final da penalidade aplicada')
    descricaoBloqueio: str = Field(description='Descrição livre do bloqueio aplicado. ')
    tipoDecisaoBloqueio: int = Field(description='Origem da decisão do Bloqueio: 1 ou 2')
    descricaoDecisaoBloqueio: str = Field(description='Descrição da decisão bloqueio:  1 – Decisão Judicial   2 – Decisão Administrativa')
    recolhimentoCnhBloqueada: bool = Field(description='Informa se a CNH foi recolhida:  1 – Sim  2 – Não')
    requisitosLiberacaoBloqueio: str = Field(description='Indica quais os Cursos/Exames deve ser realizados para a Liberação do Bloqueio.')
    prazoPenalBloqueio: int = Field(description='Identifica o tempo de penalidade.')
    tipoPrazoPenalBloqueio: int = Field(description='Indica qual o tipo de prazo para o campo Prazo Penalidade: 1, 2, 3.')
    descricaoPrazoBloqueio: str = Field(description='Descrição do tipo prazo penalidade: 1 – Dia, 2 – Mes,  3 – Ano')
    prazoPenalTotalBloqueio: int = Field(description='Identifica o tempo de penalidade total para bloqueios da mesma UF e Motivo Bloqueio. ')
    tipoPrazoTotalBloqueio: int = Field(description='Indica qual o tipo de prazo para o campo Prazo Penalidade Total: 1,  2, 3.')
    descricaoPrazoTotalBloqueio: str = Field(description='Descrição do tipo de prazo para o campo Prazo Penalidade Total: 1 – Dia, 2 – Mes e 3 – Ano')
#    DT_MVM_DWS: datetime.date = Field(description='Data de movimentação do Arquivo')
#    DH_CRG_DWS: datetime.date = Field(description='Data e Hora que o registros entrou na tabela')
#    CD_VRF: str = Field(description='Código de verificação ')
#    IN_EXL: int = Field(description='Indicador de Exclusão')

    class Config:
        orm_mode = True
