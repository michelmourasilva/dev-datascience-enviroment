from typing import Optional, List, ForwardRef, Any
from pydantic import validator, BaseModel, Field
import datetime
from schemas.enumerators import Enum_EstadosBr, Enum_permissionario, Enum_sexo, Enum_nacionalidade
from schemas.bloqueio import BloqueioBaseSchema
import re
from core.util import optional_validator


@optional_validator(
                    # "NU_CONTROLE_CONDUTOR",
                    "dataCadastramento",
                    "dataNascimento",
                    "dataTransacaoUltimaAtualizacao",
                    "dataValidadeCnh",
                    "dataPrimeiraHabilitacao",
                    "dataUltimaEmissaoHistorico",
                    # "DT_SITUACAO_CNH_HEMI",
                    "dataValidadePid",
                    "dataValidadeHabilitacaoEstrangeira",
                    "dataCursoTpp",
                    "dataCursoTe",
                    "dataCursoTcp",
                    "dataCursoTve",
                    "dataCursoTci",
                    "dataCursoTmt",
                    "dataCursoTmf",
                    "dataCursoReciclagemInfrator",
                    "dataCursoAtualizacaoRenovacaoCnh",
                    # "DT_MVM_DWS",
                    # "DH_CRG_DWS",
                    "ocorrencias"
                    )
class CadastroBaseSchema(BaseModel):
#    NU_CONTROLE_CONDUTOR: int = Field(description='Numero de Controle dos Condutores. Identifica de forma única o Condutor, evitando redundancias encontradas no Cadastro Nacional de Pessoa Fisica - CPF')
    cpf: str = Field(description='Número do Cadastro de Pessoa Fisica')
    ufDominio: str = Field(description='Sigla da Unidade da Federação detentora do prontuário do Candidato ou Condutor')
    numeroFormularioRenach: str = Field(description='Número do Formulário RENACH do Candidato ou Condutor')
    numeroRegistro: str = Field(description='Numero de registro da Carteira Nacional de Habilitação - CNH. ')
    numeroFormularioCnh: str = Field(description='Numero do formulário da Carteira Nacional de Habilitação do Condutor, informado pela gráfica emissora. ')
    numeroPgu: str = Field(description='Número do Prontuário Geral da União - PGU')
    dataCadastramento: Any = Field(description='Data de cadastro do candidato no Departamento de Transito.')
    numeroListaImpedimento: str = Field(description='Número gerado pela BINCO para identificar um impedimento.')
    permissionario: int = Field(description='Identifica se o Condutor é permissionário: 1 - SIM 2 - NÃO 3 - NOVA PERMISSAO')
    ufSolicitanteTransferencia: str = Field(description='Sigla da Unidade da Federação que esta solicitando a transferencia.')
    nome: str = Field(description='Nome do Cidadão Candidato a Carteira Nacional de Habilitação, ou Condutor')
    dataNascimento: Any = Field(description='Data de nascimento do Candidato ou Condutor')
    localidadeNascimento: str = Field(description='Código do Municipio IBGE ou do País de nascimento do Candidato ou Condutor')
    descricaoLocalidadeNascimento: str = Field(description='Descrição do Municipio de nascimento do Candidato ou Condutor')
    sexo: int = Field(description='Código que identifica o sexo do Candidato ou Condutor 0 - INEXISTENTE 1 - MASCULINO 2 - FEMININO')
    descricaoSexo: str = Field(description='Descrição do Sexo do Candidato ou Condutor 0 - INEXISTENTE 1 - MASCULINO 2 - FEMININO')
    nomeMae: str = Field(description='Nome da Mãe do Candidato ou Condutor')
    nomePai: str = Field(description='Nome do Pai do Candidato ou Condutor')
    enderecoLogradouro: str = Field(description='Nome da Rua, Avenida, Praça, Etc. do endereço informado pelo Candidato ou Condutor')
    enderecoNumero: str = Field(description='Identifica o número da casa, apartamento, loja e etc. ')
    enderecoComplemento: str = Field(description='Complemento do Endereço do Candidato ou Condutor')
    enderecoBairro: str = Field(description='Bairro onde esta localizado o endereço do Candidato ou Condutor')
    enderecoCep: str = Field(description='Numero do Código do Endereçamento Postal do endereço do Candidato ou Condutor')
    enderecoMunicipio: str = Field(description='Código do Municipio referente ao endereço do Candidato ou Condutor')
    descricaoEnderecoMunicipio: str = Field(description='Nome do Municipio de localização do Endereço')
    enderecoUf: str = Field(description='Sigla da Unidade da Federação do Municipio do Endereço')
    nacionalidade: int = Field(description='Nacionalidade do Candidato ou Condutor 1 - Brasileiro 2 - Brasileiro naturalizado 3 - Estrangeiro 4 - Brasileiro nascido no exterior')
    descricaoNacionalidade: str = Field(description='Descrição da Nacionalidade: 1 - Brasileiro 2 - Brasileiro naturalizado 3 - Estrangeiro 4 - Brasileiro nascido no exterior')
    tipoDocumento: int = Field(description='Codigo do tipo de documento de identidade apresentado: 0 - Inexistente 1 - Carteira de identidade 2 - Carteira profissional 3 - Passaporte 4 - Certificado de reservista')
    descricaoDocumento: str = Field(description='Descrição do documento de identidade apresentado 0 - Inexistente 1 - Carteira de identidade 2 - Carteira profissional 3 - Passaporte 4 - Certificado de reservista')
    numeroDocumento: str = Field(description='Numero do documento de identificação apresentado')
    orgaoExpedidorDocumento: str = Field(description='Descrição do Orgão emissor do Documento apresentado pelo Candidato ou Condutor')
    ufExpedidorDocumento: str = Field(description='Sigla da Unidade da Federação onde o documento foi emitido.')
    dataTransacaoUltimaAtualizacao: Any = Field(description='Data informada da ultima atualização do registro')
    codigoTransacaoUltimaAtualizacao: int = Field(description='Código de data da ultima atualização do registro')
    categoriaAtual: str = Field(description='A categoria informada para a ultima Carteira Nacional de Habilitação registrada no Historico de Emissões - HEMI.')
    categoriaRebaixada: str = Field(description='Maior categoria emitida para o Condutor e que foi rebaixada.')
    categoriaAutorizada: str = Field(description='Maior categoria informada nos eventos de Curso / Exame que preencher todos os requisitos necessários a autorização da emissão da nova Cadastro Nacional de Habilitação - CNH')
    dataValidadeCnh: Any = Field(description='Data de validade da Carteira Nacional de Habilitação')
    dataPrimeiraHabilitacao: Any = Field(description='Data que foi autorizada a emissão da primeira habilitação do Candidato ou Condutor. ')
    ufPrimeiraHabilitacao: str = Field(description='Sigla da Unidade da Federação em que foi autorizada a primeria habilitação do Candidato ou Condutor. ')
#    NU_SEGURANCA: int = Field(description='Número gerado a partir de algoritmo específico e de propriedade do Departamento Nacional de Transito - DENATRAN, composto pelos dados individuais de cada Carteira Nacional de Habilitacao, permitindo a validação da habilitação emitida')
    quadroObservacoesCnh: str = Field(description='Informa as restrições ou especializações, expressas no quadro de observações da cédula da Carteira Nacional de Habilitação, expedida para o Condutor RENACH.')
    ufHabilitacaoAtual: str = Field(description='Sigla da Unidade da Federação do municipio onde foi emitida a Carteira Nacional de Habilitação')
#    CD_LOCAL_EMISSAO: str = Field(description='Código do municipio onde foi emitida a Carteira Nacional de Habilitação.')
#    DS_LOCAL_EMISSAO: str = Field(description='Descrição do Municipio onde foi emitida a Carteira Nacional de Habilitação.')
    dataUltimaEmissaoHistorico: Any = Field(description='Data em foi emitida peça grafica, a Carteira NAACIONAL DE habilitação ')
    situacaoCnh: str = Field(description='Código que identifica a situação da Carteira Nacional de Habilitação: 0 - Inexistente 1 - Emissao autorizada 2 - Em emissao 3 - Emitida 4 - Confirmada A - Cancelada erro DETRAN B - Cancelada erro gráfica Z - Cancelada outros motivos C - Cancelado fraude')
    descricaoSituacaoCnh: str = Field(description='Descrição da situação: 0 - Inexistente 1 - Emissao autorizada 2 - Em emissao 3 - Emitida 4 - Confirmada A - Cancelada erro DETRAN B - Cancelada erro gráfica Z - Cancelada outros motivos C - Cancelado fraude')
    situacaoCnhAnterior: str = Field(description='Código que identifica a situação da Carteira Nacional de Habilitação anterior a atual 0 - Inexistente 1 - Emissao autorizada 2 - Em emissao 3 - Emitida 4 - Confirmada A - Cancelada erro DETRAN B - Cancelada erro Grafica Z - Cancelada outros motivos C - Cancelada fraude ')
    descricaoSituacaoCnhAnterior: str = Field(description='Descrição da situação: 0 - Inexistente 1 - Emissao autorizada 2 - Em emissao 3 - Emitida 4 - Confirmada A - Cancelada erro DETRAN B - Cancelada erro Grafica Z - Cancelada outros motivos C - Cancelada fraude ')
#    DT_SITUACAO_CNH_HEMI: datetime.date = Field(description='Data de registro da ultima situação da Carteira Nacional de Habilitação')
    motivoRequerimento1: str = Field(description='Código do motivo que identifica o tipo de requerimento')
    descricaoMotivoRequerimento1: str = Field(description='Descrição do motivo do requerimento: 1 – PRIMEIRA HABILITAÇÃO  2 – SEGUNDA VIA  3 – REGISTRO ESTRANGEIRO  4 – REGISTRO  5 – RENOVAÇÃO DE EXAMES  6 – MUDANÇA DE CATEGORIA  7 – ADIÇÃO DE CATEGORIA  8 – ALTERAÇÃO DE DADOS  9 – REABILITAÇÃO  C – CNH DEFINITIVA  D – CNH FAIXA DOURADA  E – NOVO PROCESSO DE HABILITAÇÃO ')
    motivoRequerimento2: str = Field(description='Codigo do motivo do requerimento associado a CNH 1 – Primeira habilitação; 2 – Segunda via; 3 – Registro estrangeiro; 4 – Registro; 5 – Renovação de exames; 6 – Mudança de categoria; 7 – Adição de categoria; 8 – Alteração de dados; 9 – Reabilitação; C – CNH definitiva; D – CNH faixa Dourada;e, E – Novo Processo de Habilitação')
    descricaoMotivoRequerimento2: str = Field(description='Descrição do motivo do requerimento: 1 – Primeira habilitação; 2 – Segunda via; 3 – Registro estrangeiro; 4 – Registro; 5 – Renovação de exames; 6 – Mudança de categoria; 7 – Adição de categoria; 8 – Alteração de dados; 9 – Reabilitação; C – CNH definitiva; D – CNH faixa Dourada;e, E – Novo Processo de Habilitação')
    motivoRequerimento3: str = Field(description='Codigo do motivo do requerimento associado a CNH 1 – Primeira habilitação; 2 – Segunda via; 3 – Registro estrangeiro; 4 – Registro; 5 – Renovação de exames; 6 – Mudança de categoria; 7 – Adição de categoria; 8 – Alteração de dados; 9 – Reabilitação; C – CNH definitiva; D – CNH faixa Dourada;e, E – Novo Processo de Habilitação')
    descricaoMotivoRequerimento3: str = Field(description='Descrição do motivo do requerimento: 1 – Primeira habilitação; 2 – Segunda via; 3 – Registro estrangeiro; 4 – Registro; 5 – Renovação de exames; 6 – Mudança de categoria; 7 – Adição de categoria; 8 – Alteração de dados; 9 – Reabilitação; C – CNH definitiva; D – CNH faixa Dourada;e, E – Novo Processo de Habilitação')
    motivoRequerimento4: str = Field(description='Codigo do motivo do requerimento associado a CNH 1 – Primeira habilitação; 2 – Segunda via; 3 – Registro estrangeiro; 4 – Registro; 5 – Renovação de exames; 6 – Mudança de categoria; 7 – Adição de categoria; 8 – Alteração de dados; 9 – Reabilitação; C – CNH definitiva; D – CNH faixa Dourada;e, E – Novo Processo de Habilitação')
    descricaoMotivoRequerimento4: str = Field(description='Descrição do motivo do requerimento: 1 – Primeira habilitação; 2 – Segunda via; 3 – Registro estrangeiro; 4 – Registro; 5 – Renovação de exames; 6 – Mudança de categoria; 7 – Adição de categoria; 8 – Alteração de dados; 9 – Reabilitação; C – CNH definitiva; D – CNH faixa Dourada;e, E – Novo Processo de Habilitação')
    numeroFormularioPid: str = Field(description='Numero do formulário Permissão Internacional para Dirigir - PID')
    dataValidadePid: Any = Field(description='Data limite de validade da Permissão Internacional para Dirigir, expedida por Órgão de Trânsito no Brasil.')
    ufExpedicaoPid: str = Field(description='Sigla da Unidade da Federação onde foi expedida a Permissão Internacional para Dirigir.')
    numeroFormularioCnhBasePid: str = Field(description='Número do formulário da Carteira Nacional de Habilitação  (tipográfico) do condutor utilizado como base de informações para a emissão da Permissão Internacional para Dirigir.')
    motivoRequerimentoPid1: str = Field(description='Código do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica')
    descricaoMotivoRequerimentoPid1: str = Field(description='Descrição do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica')
    motivoRequerimentoPid2: str = Field(description='Código do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica')
    descricaoMotivoRequerimentoPid2: str = Field(description='Descrição do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica ')
    motivoRequerimentoPid3: str = Field(description='Código do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica')
    descricaoMotivoRequerimentoPid3: str = Field(description='Descrição do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica ')
    motivoRequerimentoPid4: str = Field(description='Código do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica')
    descricaoMotivoRequerimentoPid4: str = Field(description='Descrição do motivo para requerimento associado a emissão da Permissão Internacional para Dirigir E - primeira emissao / atualizacao 2 - segunda via A - reemissao - erro detran B - reemissao - erro grafica')
    situacaoPid: str = Field(description='Código que identifica a situação da Permissão Internacional para Dirigir expedida por Órgão de Trânsito no Brasil. 0 - inexistente  1 - emissão autorizada  2 - em emissão  3 - emitida  4 - confirmada  A - cancelada-erro detran  B - cancelada-erro gráfica  C - cancelada por fraude  Z - cancelada-outros motivos')
#    DS_SITUACAO_PID: str = Field(description='Descrição da situação do pedido internacional para digirir  0 - inexistente  1 - emissão autorizada  2 - em emissão  3 - emitida  4 - confirmada  A - cancelada-erro detran  B - cancelada-erro gráfica  C - cancelada por fraude  Z - cancelada-outros motivos')
    registroNacionalEstrangeiro: str = Field(description='Dados do documento de identificação do cidadão estrangeiro expedido em território nacional pela Polícia Federal.')
    paisOrigemHabilitacaoEstrangeira: str = Field(description='Códido do pais de origem do estrangeiro que requer habilitação ou permissão internacional para dirigir ')
    descricaoPaisOrigemHabilitacaoEstrangeira: str = Field(description='Nome do País em acordo com tabela corporativa do Departamento Nacional de Transito')
    identificacaoHabilitacaoEstrangeira: str = Field(description='Número ou chave de identificação do condutor e, a identificação do documento e órgão expedidor da habilitação no país estrangeiro.')
    dataValidadeHabilitacaoEstrangeira: Any = Field(description='Data de Validade da Habilitação Estrangeira.')
    restricoesMedicas: str = Field(description='Descrição de restrições médicas que impeçam ou delimitem a possibilidade de requerer habilitação')
    classificacaoCursoTpp: str = Field(description='Classificação Curso de Transporte de Produtos Perigoso:     E  para Curso TPP = 01     A  para Curso TPP = 11')
    descricaoClassificacaoCursoTpp: str = Field(description='Descrição do tipo de Curso de Transporte de Produtos Perigosos - TPP:  0 - Inexistente,   01 – Curso especialização    11 - Curso de atualização')
    dataCursoTpp: Any = Field(description='Data de inclusao do Curso TPP')
    ufCursoTpp: str = Field(description='Sigla da Unidade da Federação do Municipio onde o curso foi incluido ')
    classificacaoCursoTe: str = Field(description='Classificação Curso Transporte Escolar:     E  para Curso TE = 02    A  para Curso TE = 12')
    descricaoClassificacaoCursoTe: str = Field(description='Descrição do tipo de Curso de Transporte Escolar - TE:  0 - Inexistente 02 – Curso de especialização    12 - Curso de atualização ')
    ufCursoTe: str = Field(description='Sigla da Unidade da Federação one o curso foi incluido')
    dataCursoTe: Any = Field(description='Data de inclusão do curso')
    classificacaoCursoTcp: str = Field(description='Classificação Curso Transporte Coletivo de Passageiros:   E  para Curso TCP = 03     A  para Curso TCP = 13')
    descricaoClassificacaoCursoTcp: str = Field(description='Descrição do tipo de curso de Transporte Coletivo de Passageiros - TCP:  0 - Inexistente 03 – Curso de especialização    13 – Curso de atualização')
    ufCursoTcp: str = Field(description='Sigla da Unidade da Federação onde o curso foi incluido')
    dataCursoTcp: Any = Field(description='Data de inclusão de curso')
    classificacaoCursoTve: str = Field(description='Codigo de classificação do curso de Transporte de Veiculos de Emergencia')
    descricaoClassificacaoCursoTve: str = Field(description='Descrição do tipo de curos de Transporte de Veiculos de Emergencia - TVE:  0 - Inexistente 04 – Curso de especialização    14 - Curso de atualização ')
    ufCursoTve: str = Field(description='Sigla da Unidade de Federação do curso ')
    dataCursoTve: Any = Field(description='Data de inclusão do Curso')
    classificacaoCursoTci: str = Field(description='Classificação Curso Transporte de cargas Indivisiveis - TCI: E  para Curso TMT = 08     A  para Curso TMT = 18')
    descricaoClassificacaoCursoTci: str = Field(description='Descrição do tipo de curso de Curso Transporte de cargas Indivisiveis - TCI::  0 - Inexistente 07 - Curso de especialização   17 – Curso de atualização')
    ufCursoTci: str = Field(description='Sigla da Unidade da Federação onde o Curso foi incluido')
    dataCursoTci: Any = Field(description='Data de inclusão do Curso')
    classificacaoCursoTmt: str = Field(description='Classificação Curso Transporte Mototaxista - TMT:    E  para Curso TMT = 08     A  para Curso TMT = 18')
    descricaoClassificacaoCursoTmt: str = Field(description='Descrição:  0 - Inexistente 08 - Curso de especialização   18 - Curso de atualização')
    ufCursoTmt: str = Field(description='Sigla da Unidade da Federação onde o Curso foi incluido')
    dataCursoTmt: Any = Field(description='Data de inclusão do Curso')
    classificacaoCursoTmf: str = Field(description='Classificação Curso Transporte Motofretista - TMF:   E  para Curso TMF = 09     A  para Curso TMF = 19')
    descricaoClassificacaoCursoTmf: str = Field(description='Descrição do tipo de curso de Transporte de MotoFrentista -TMF:  0 - INEXISTENTE,   09 - CURSO DE ESPECIALIZAÇÃO   19 - CURSO DE ATUALIZAÇÃO')
    ufCursoTmf: str = Field(description='Sigla da Unidade da Federação onde o Curso foi incluido')
    dataCursoTmf: Any = Field(description='Data de inclusão do Curso')
    ufCursoReciclagemInfrator: str = Field(description='Sigla da Unidade de Federação do curso ')
    dataCursoReciclagemInfrator: Any = Field(description='Data de inclusão do Curso ')
    modalidadeCursoReciclagemInfrator: str = Field(description='Modalidade do curso de reciclagem:  0 - Inexistente; 1 - Presencial integral 2 - Ensino a distancia 3 - Aproveitamento de estudos (comprovado) 4 - Presencial(parcial) com ensino a distancia/autodidata e/ou aproveitamento de estudos; e, 5 - Ensino a distância/auto-didata com aproveitamento de estudos')
    descricaoModalidadeCursoReciclagemInfrator: str = Field(description='Modalidades 0 - Inexistente 1 - Presencial Integral 2 - Ensino a Distancia 3 - Aproveitamento de estudos (comprovado) 4 - Presencial (parcial) com ensino a distância / autodidata  5 - Ensino a distancia / autodidata com aproveitamento nos estudos')
    ufCursoAtualizacaoRenovacaoCnh: str = Field(description='Sigla da Unidade de Federação onde o Curso foi incluido')
    dataCursoAtualizacaoRenovacaoCnh: Any = Field(description='Data de inclusão do Curso')
    modalidadeCursoAtualizacaoRenovacaoCnh: str = Field(description='Modalidades: 0 - Inexistente; 1 - Presencial integral; 2 - Ensino a distância; 3 - Aproveitamento de estudos(comprovado)  4 - Presencial (parcial) com ensino a distancia / autodidata e ou aproveitamento nos estudos 5 - Ensino a distância / autodidata com aproveitamento de estudos ')
    quantidadeOcorrenciasImpedimentos: int = Field(description='Quantidade de bloqueios / impedimentos do cidadão')
    descricaoModalidadeCursoAtualizacaoRenovacaoCnh: str = Field(description='Descrição Modalidade Curso Atualização Renovação CNH')
    cancelamento: str = Field(description='Campo descontinuado, mantido apenas para compatibilidade', default='')
#    situacaoExclusaoCondutor: str = Field(description='Indicador de que o condutor foi excluído da BANCO.  Para o condutor excluído este campo apresenta o indicativo = “S”,  Caso contrário estará em branco.')
#    DT_MVM_DWS: datetime.date = Field(description='Data de movimentação do arquivo')
#    DH_CRG_DWS: datetime.date = Field(description='Data e Hora que o registros entrou na tabela')
#    CD_VRF: str = Field(description='Código de Verificação')
#    IN_EXL: int = Field(description='Indicador de Exclusão')

    ocorrencias: List[BloqueioBaseSchema]

    @validator("ocorrencias")
    def options_non_empty(cls, v):
        return None if len(v) == 0 else v

#   @validator("dh_crg_dws")
#   def validate_datetime(cls, v: datetime.datetime, **kwargs) -> datetime.datetime:
#       if v > datetime.datetime.now():
#           raise ValueError(
#               "A data não pode estar no futuro!"
#           )
#       return v
#
#   @validator("nu_cep")
#   def validate_postal_code(cls, v: str, **kwargs: int) -> str:
#
#       if v is not None:
#           CEP_REGEX = re.compile("[0-9]{5}\\-[0-9]{3}")
#
#           if not CEP_REGEX.match(nu_cep := v.rjust(9, "0")):
#               raise ValueError("O CEP informado é inválido!")
#           return nu_cep

    class Config:
        orm_mode = True

@optional_validator('condutor')
class CondutorBase(BaseModel):
    quantidade: int
    quantidadeReal: int
    idUltimoRegistro: int
    condutor: List[CadastroBaseSchema]
