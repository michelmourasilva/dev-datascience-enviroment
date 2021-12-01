from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, CHAR
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Date, DateTime
from core.database import Base
from src.env import DATABASE_SCHEMA
import models.bloqueio as bloqueio
from core.util import retorno_data
import unidecode

class CadastroDB(Base):
    __tablename__ = "tb_cadastro_renach"
    __table_args__ = {'schema': DATABASE_SCHEMA}


    # Comentado pois foi identificado que a chave entre a tabela cadastro e bloqueio é o CPF
    NU_CONTROLE_CONDUTOR = Column('nu_controle_condutor', Numeric(11, 0), nullable=False, primary_key=True)
    cpf = Column('nu_cpf', String(11), nullable=False)

    ufDominio = Column('sg_uf_dominio', String(2), nullable=True)
    numeroFormularioRenach = Column('nu_formulario_renach', String(11), nullable=False)
    _numeroRegistro = Column('nu_registro', Numeric(11, 0), nullable=False)
    _numeroFormularioCnh = Column('nu_formulario_cnh', Numeric(10, 0), nullable=False)
    _numeroPgu = Column('nu_pgu', Numeric(9, 0), nullable=True)
    _dataCadastramento = Column('dt_cadastro', Date, nullable=True)
    _numeroListaImpedimento = Column('nu_lista_impedimento', Numeric(11, 0), nullable=True)
    permissionario = Column('nu_permissionario', Numeric(1, 0), nullable=True)
    ufSolicitanteTransferencia = Column('sg_uf_solicita_transf', String(2), nullable=True)
    nome = Column('no_individuo', String(44), nullable=True)
    _dataNascimento = Column('dt_nascimento', Date, nullable=True)
    localidadeNascimento = Column('cd_local_nascimento', String(5), nullable=True)
    descricaoLocalidadeNascimento = Column('ds_local_nascimento', String(30), nullable=True)
    _sexo = Column('cd_sexo', Numeric(1, 0), nullable=True)
    descricaoSexo = Column('ds_sexo', String(11), nullable=True)
    nomeMae = Column('no_mae', String(44), nullable=True)
    nomePai = Column('no_pai', String(44), nullable=True)
    enderecoLogradouro = Column('ds_endereco_logradouro', String(50), nullable=True)
    enderecoNumero = Column('nu_endereco', String(10), nullable=True)
    enderecoComplemento = Column('ds_endereco_complemento', String(30), nullable=True)
    enderecoBairro = Column('ds_endereco_bairro', String(30), nullable=True)
    _enderecoCep = Column('nu_cep', Numeric(8, 0), nullable=True)
    _enderecoMunicipio = Column('cd_municipio', Numeric(5, 0), nullable=True)
    descricaoEnderecoMunicipio = Column('ds_endereco_municipio', String(30), nullable=True)
    enderecoUf = Column('sg_uf_endereco', String(2), nullable=True)
    nacionalidade = Column('cd_nacionalidade', Numeric(1, 0), nullable=True)
    _descricaoNacionalidade = Column('ds_nacionalidade', String(30), nullable=True)
    tipoDocumento = Column('cd_documento_id', Numeric(1, 0), nullable=True)
    descricaoDocumento = Column('ds_documento_id', String(22), nullable=True)
    numeroDocumento = Column('nu_documento_id', String(15), nullable=True)
    orgaoExpedidorDocumento = Column('ds_orgao_emissor', String(10), nullable=True)
    ufExpedidorDocumento = Column('sg_uf_orgao_emissor', String(2), nullable=True)
    _dataTransacaoUltimaAtualizacao = Column('dt_ultima_atualizacao', Date, nullable=True)
    codigoTransacaoUltimaAtualizacao = Column('cd_ultima_atualizacao', Numeric(3, 0), nullable=True)
    categoriaAtual = Column('ds_categoria_atual', String(4), nullable=True)
    _categoriaRebaixada = Column('ds_categoria_rebaixada', String(4), nullable=True)
    categoriaAutorizada = Column('ds_categoria_autorizada', String(4), nullable=True)
    _dataValidadeCnh = Column('dt_validade_cnh', Date, nullable=True)
    _dataPrimeiraHabilitacao = Column('dt_primeira_cnh', Date, nullable=True)
    ufPrimeiraHabilitacao = Column('sg_uf_primeira_cnh', String(2), nullable=True)
    NU_SEGURANCA = Column('nu_seguranca', Numeric(11, 0), nullable=True)
    quadroObservacoesCnh = Column('ds_observacao_cnh', String(20), nullable=True)
    ufHabilitacaoAtual = Column('sg_uf_cnh', String(2), nullable=True)
    CD_LOCAL_EMISSAO = Column('cd_local_emissao', String(5), nullable=True)
    DS_LOCAL_EMISSAO = Column('ds_local_emissao', String(30), nullable=True)
    _dataUltimaEmissaoHistorico = Column('dt_emissao_cnh', Date, nullable=True)
    situacaoCnh = Column('st_cnh_hemi', String(1), nullable=True)
    descricaoSituacaoCnh = Column('ds_situacao_cnh_hemi', String(20), nullable=True)
    situacaoCnhAnterior = Column('cd_situacao_cnh_anterior', String(1), nullable=True)
    descricaoSituacaoCnhAnterior = Column('ds_situacao_cnh_anterior', String(20), nullable=True)
    DT_SITUACAO_CNH_HEMI = Column('dt_situacao_cnh_hemi', Date, nullable=True)
    motivoRequerimento1 = Column('cd_motivo_requ_01', String(1), nullable=True)
    _descricaoMotivoRequerimento1 = Column('ds_motivo_requ_01', String(30), nullable=True)
    motivoRequerimento2 = Column('cd_motivo_requ_02', String(1), nullable=True)
    _descricaoMotivoRequerimento2 = Column('ds_motivo_requ_02', String(30), nullable=True)
    motivoRequerimento3 = Column('cd_motivo_requ_03', String(1), nullable=True)
    _descricaoMotivoRequerimento3 = Column('ds_motivo_requ_03', String(30), nullable=True)
    motivoRequerimento4 = Column('cd_motivo_requ_04', String(1), nullable=True)
    _descricaoMotivoRequerimento4 = Column('ds_motivo_requ_04', String(30), nullable=True)
    _numeroFormularioPid = Column('nu_formulario_pid', Numeric(9, 0), nullable=True)
    _dataValidadePid = Column('dt_validade_pid', Date, nullable=True)
    ufExpedicaoPid = Column('sg_uf_expedicao_pid', String(2), nullable=True)
    _numeroFormularioCnhBasePid = Column('nu_formulario_cnh_pid', Numeric(10, 0), nullable=True)
    motivoRequerimentoPid1 = Column('cd_motiva_requ_pid_01', String(1), nullable=True)
    _descricaoMotivoRequerimentoPid1 = Column('ds_motiva_requ_pid_01', String(30), nullable=True)
    motivoRequerimentoPid2 = Column('cd_motiva_requ_pid_02', String(1), nullable=True)
    _descricaoMotivoRequerimentoPid2 = Column('ds_motiva_requ_pid_02', String(30), nullable=True)
    motivoRequerimentoPid3 = Column('cd_motiva_requ_pid_03', String(1), nullable=True)
    _descricaoMotivoRequerimentoPid3 = Column('ds_motiva_requ_pid_03', String(30), nullable=True)
    motivoRequerimentoPid4 = Column('cd_motiva_requ_pid_04', String(1), nullable=True)
    _descricaoMotivoRequerimentoPid4 = Column('ds_motiva_requ_pid_04', String(30), nullable=True)
    situacaoPid = Column('st_situacao_pid', String(1), nullable=True)
    DS_SITUACAO_PID = Column('ds_situacao_pid', String(25), nullable=True)
    registroNacionalEstrangeiro = Column('nu_reg_nacional_estrangeiro', String(27), nullable=True)
    paisOrigemHabilitacaoEstrangeira = Column('cd_pais_habilita_estrangeiro', String(5), nullable=True)
    _descricaoPaisOrigemHabilitacaoEstrangeira = Column('ds_pais_origem', String(30), nullable=True)
    identificacaoHabilitacaoEstrangeira = Column('id_habilitacao_estrangeira', String(30), nullable=True)
    _dataValidadeHabilitacaoEstrangeira = Column('dt_validade_cnh_estrangeiro', Date, nullable=True)
    restricoesMedicas = Column('ds_restricao_medica', String(88), nullable=True)
    classificacaoCursoTpp = Column('cd_classifica_curso_tpp', String(1), nullable=True)
    _descricaoClassificacaoCursoTpp = Column('ds_classifica_curso_tpp', String(20), nullable=True)
    _dataCursoTpp = Column('dt_curso_tpp', Date, nullable=True)
    ufCursoTpp = Column('sg_uf_curso_tpp', String(2), nullable=True)
    classificacaoCursoTe = Column('cd_classifica_curso_te', String(1), nullable=True)
    _descricaoClassificacaoCursoTe = Column('ds_classifica_curso_te', String(20), nullable=True)
    ufCursoTe = Column('sg_uf_curso_te', String(2), nullable=True)
    _dataCursoTe = Column('dt_curso_te', Date, nullable=True)
    classificacaoCursoTcp = Column('cd_classifica_curso_tcp', String(1), nullable=True)
    _descricaoClassificacaoCursoTcp = Column('ds_classifica_curso_tcp', String(30), nullable=True)
    ufCursoTcp = Column('sg_uf_curso_tcp', String(2), nullable=True)
    _dataCursoTcp = Column('dt_curso_tcp', Date, nullable=True)
    classificacaoCursoTve = Column('cd_classifica_curso_tve', String(1), nullable=True)
    _descricaoClassificacaoCursoTve = Column('ds_classifica_curso_tve', String(30), nullable=True)
    ufCursoTve = Column('sg_uf_curso_tve', String(2), nullable=True)
    _dataCursoTve = Column('dt_curso_tve', Date, nullable=True)
    classificacaoCursoTci = Column('cd_classifica_curso_tci', String(1), nullable=True)
    _descricaoClassificacaoCursoTci = Column('ds_classifica_curso_tci', String(20), nullable=True)
    ufCursoTci = Column('sg_uf_curso_tci', String(2), nullable=True)
    _dataCursoTci = Column('dt_curso_tci', Date, nullable=True)
    classificacaoCursoTmt = Column('cd_classifica_curso_tmt', String(1), nullable=True)
    _descricaoClassificacaoCursoTmt = Column('ds_classifica_curso_tmt', String(20), nullable=True)
    ufCursoTmt = Column('sg_uf_curso_tmt', String(2), nullable=True)
    _dataCursoTmt = Column('dt_curso_tmt', Date, nullable=True)
    classificacaoCursoTmf = Column('cd_classifica_curso_tmf', String(1), nullable=True)
    _descricaoClassificacaoCursoTmf = Column('ds_classifica_curso_tmf', String(20), nullable=True)
    ufCursoTmf = Column('sg_uf_curso_tmf', String(2), nullable=True)
    _dataCursoTmf = Column('dt_curso_tmf', Date, nullable=True)
    ufCursoReciclagemInfrator = Column('sg_uf_curso_reciclagem', String(2), nullable=True)
    _dataCursoReciclagemInfrator = Column('dt_curso_reciclagem', Date, nullable=True)
    modalidadeCursoReciclagemInfrator = Column('cd_modalidade_curso_recicla', String(1), nullable=True)
    _descricaoModalidadeCursoReciclagemInfrator = Column('ds_modalidade_curso_recicla', String(75), nullable=True)
    ufCursoAtualizacaoRenovacaoCnh = Column('sg_uf_curso_renova_cnh', String(2), nullable=True)
    _dataCursoAtualizacaoRenovacaoCnh = Column('dt_curso_renova_cnh', Date, nullable=True)
    _modalidadeCursoAtualizacaoRenovacaoCnh = Column('cd_modalidade_renova_cnh', String(1), nullable=True)
    quantidadeOcorrenciasImpedimentos = Column('qt_ocorrencia_impedimento', Numeric(3, 0), nullable=True)
    situacaoExclusaoCondutor = Column('st_exclusao_condutor', String(1), nullable=True)
    DT_MVM_DWS = Column('dt_mvm_dws', Date, nullable=False)
    DH_CRG_DWS = Column('dh_crg_dws', DateTime, nullable=False)
    CD_VRF = Column('cd_vrf', String(32), nullable=False)
    IN_EXL = Column('in_exl', Numeric(32, 0), nullable=False)
    _descricaoModalidadeCursoAtualizacaoRenovacaoCnh = Column('ds_modal_curso_renova_cnh', String(75), nullable=True)

    ocorrencias = relationship('bloqueio.BloqueioDB', viewonly=True, lazy='joined')

    @property
    def numeroRegistro(self):
        return str(self._numeroRegistro).rjust(11, '0')

    @property
    def numeroFormularioCnh(self):
        return str(self._numeroFormularioCnh).rjust(10, '0')

    @property
    def numeroListaImpedimento(self):
        return str(self._numeroListaImpedimento).rjust(11, '0')

    @property
    def sexo(self):
        return 'INEXISTENTE' if self._sexo not in (1, 2) else self._sexo

    @property
    def enderecoCep(self):
        return str(self._enderecoCep)

    @property
    def enderecoMunicipio(self):
        return str(self._enderecoMunicipio).rjust(5, '0')

    @property
    def numeroPgu(self):
        return str(self._numeroPgu).rjust(9, '0')

    @property
    def categoriaRebaixada(self):
        return self._categoriaRebaixada.strip()

    @property
    def modalidadeCursoAtualizacaoRenovacaoCnh(self):
        return self._modalidadeCursoAtualizacaoRenovacaoCnh.rjust(2, '0') if self._modalidadeCursoAtualizacaoRenovacaoCnh != '' else ''

    @property
    def numeroFormularioPid(self):
        return str(self._numeroFormularioPid).rjust(9, '0')

    @property
    def numeroFormularioCnhBasePid(self):
        return str(self._numeroFormularioCnhBasePid).rjust(10, '0')

    @property
    def descricaoMotivoRequerimento1(self):
        return unidecode.unidecode(self._descricaoMotivoRequerimento1) if self._descricaoMotivoRequerimento1 != '' else 'INEXISTENTE'

    @property
    def descricaoMotivoRequerimento2(self):
        return unidecode.unidecode(self._descricaoMotivoRequerimento2) if self._descricaoMotivoRequerimento2 != '' else 'INEXISTENTE'

    @property
    def descricaoMotivoRequerimento3(self):
        return unidecode.unidecode(self._descricaoMotivoRequerimento3) if self._descricaoMotivoRequerimento3 != '' else 'INEXISTENTE'

    @property
    def descricaoMotivoRequerimento4(self):
        return unidecode.unidecode(self._descricaoMotivoRequerimento4) if self._descricaoMotivoRequerimento4 != '' else 'INEXISTENTE'

    @property
    def descricaoNacionalidade(self):
        return self._descricaoNacionalidade if self._descricaoNacionalidade != '' else 'INEXISTENTE'

    @property
    def descricaoClassificacaoCursoTpp(self):
        return self._descricaoClassificacaoCursoTpp if self._descricaoClassificacaoCursoTpp != '' else 'INEXISTENTE'

    @property
    def descricaoClassificacaoCursoTe(self):
        return self._descricaoClassificacaoCursoTe if self._descricaoClassificacaoCursoTe != '' else 'INEXISTENTE'

    @property
    def descricaoClassificacaoCursoTcp(self):
        return self._descricaoClassificacaoCursoTcp if self._descricaoClassificacaoCursoTcp != '' else 'INEXISTENTE'

    @property
    def descricaoClassificacaoCursoTve(self):
        return self._descricaoClassificacaoCursoTve if self._descricaoClassificacaoCursoTve != '' else 'INEXISTENTE'

    @property
    def descricaoClassificacaoCursoTci(self):
        return self._descricaoClassificacaoCursoTci if self._descricaoClassificacaoCursoTci != '' else 'INEXISTENTE'

    @property
    def descricaoClassificacaoCursoTmt(self):
        return self._descricaoClassificacaoCursoTmt if self._descricaoClassificacaoCursoTmt != '' else 'INEXISTENTE'

    @property
    def descricaoClassificacaoCursoTmf(self):
        return self._descricaoClassificacaoCursoTmf if self._descricaoClassificacaoCursoTmf != '' else 'INEXISTENTE'

    @property
    def descricaoMotivoRequerimentoPid1(self):
        return self._descricaoMotivoRequerimentoPid1 if self._descricaoMotivoRequerimentoPid1 != '' else 'INEXISTENTE'

    @property
    def descricaoMotivoRequerimentoPid2(self):
        return self._descricaoMotivoRequerimentoPid2 if self._descricaoMotivoRequerimentoPid2 != '' else 'INEXISTENTE'

    @property
    def descricaoMotivoRequerimentoPid3(self):
        return self._descricaoMotivoRequerimentoPid3 if self._descricaoMotivoRequerimentoPid3 != '' else 'INEXISTENTE'

    @property
    def descricaoMotivoRequerimentoPid4(self):
        return self._descricaoMotivoRequerimentoPid4 if self._descricaoMotivoRequerimentoPid4 != '' else 'INEXISTENTE'

    @property
    def descricaoModalidadeCursoAtualizacaoRenovacaoCnh(self):
        return self._descricaoModalidadeCursoAtualizacaoRenovacaoCnh if self._descricaoModalidadeCursoAtualizacaoRenovacaoCnh != '' else 'INEXISTENTE'

    @property
    def descricaoPaisOrigemHabilitacaoEstrangeira(self):
        valor = unidecode.unidecode(self._descricaoPaisOrigemHabilitacaoEstrangeira)
        return valor if valor not in ('', 'NAO ENCONTRADO') else 'INEXISTENTE'

    @property
    def descricaoModalidadeCursoReciclagemInfrator(self):
        return self._descricaoModalidadeCursoReciclagemInfrator if self._descricaoModalidadeCursoReciclagemInfrator != '' else 'INEXISTENTE'

    @property
    def dataCadastramento(self):
        return retorno_data(self._dataCadastramento)

    @property
    def dataNascimento(self):
        return retorno_data(self._dataNascimento)

    @property
    def dataTransacaoUltimaAtualizacao(self):
        return retorno_data(self._dataTransacaoUltimaAtualizacao)

    @property
    def dataValidadeCnh(self):
        return retorno_data(self._dataValidadeCnh)

    @property
    def dataPrimeiraHabilitacao(self):
        return retorno_data(self._dataPrimeiraHabilitacao)

    @property
    def dataUltimaEmissaoHistorico(self):
        return retorno_data(self._dataUltimaEmissaoHistorico)

    @property
    def dataValidadePid(self):
        return retorno_data(self._dataValidadePid)

    @property
    def dataValidadeHabilitacaoEstrangeira(self):
        return retorno_data(self._dataValidadeHabilitacaoEstrangeira)

    @property
    def dataCursoTpp(self):
        return retorno_data(self._dataCursoTpp)

    @property
    def dataCursoTe(self):
        return retorno_data(self._dataCursoTe)

    @property
    def dataCursoTcp(self):
        return retorno_data(self._dataCursoTcp)

    @property
    def dataCursoTve(self):
        return retorno_data(self._dataCursoTve)

    @property
    def dataCursoTci(self):
        return retorno_data(self._dataCursoTci)
    
    @property
    def dataCursoTmt(self):
        return retorno_data(self._dataCursoTmt)

    @property
    def dataCursoTmf(self):
        return retorno_data(self._dataCursoTmf)

    @property
    def dataCursoReciclagemInfrator(self):
        return retorno_data(self._dataCursoReciclagemInfrator)

    @property
    def dataCursoAtualizacaoRenovacaoCnh(self):
        return retorno_data(self._dataCursoAtualizacaoRenovacaoCnh)
