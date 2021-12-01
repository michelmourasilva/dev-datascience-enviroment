from sqlalchemy import Column, Integer, String, Numeric, CHAR, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, DateTime
from core.database import Base
from src.env import DATABASE_SCHEMA
from core.util import retorno_data

class BloqueioDB(Base):
    __tablename__ = "tb_bloqueio_cnh"
    __table_args__ = {'schema': DATABASE_SCHEMA}

    # Comentado pois foi identificado que a chave entre a tabela cadastro e bloqueio é o CPF
    seq_bloqueio_cnh = Column('seq_bloqueio_cnh', Numeric(11, 0), nullable=False, primary_key=True)
    NU_CONTROLE_CONDUTOR = Column('nu_controle_condutor', ForeignKey('{}.tb_cadastro_renach.nu_controle_condutor'.format(DATABASE_SCHEMA)), nullable=False, primary_key=True)
    cpf = Column('nu_cpf', String(11), nullable=False)
    ufDetranBloqueio = Column('sg_uf_detran', String(2), nullable=True)
    _dataImpedimentoBloqueio = Column('dt_bloqueio', Date, nullable=True)
    motivoImpedimentoBloqueio = Column('cd_bloqueio', String(1), nullable=True)
    descricaoMotivoImpedimentoBloqueio = Column('ds_codigo_bloqueio', String(30), nullable=True)
    orgaoResponsavelImpedimentoBloqueio = Column('cd_orgao_gerador', Numeric(2, 0), nullable=True)
    documentoGeradorImpedimentoBloqueio = Column('ds_documento_gerador', String(30), nullable=True)
    _dataInicioImpedimentoBloqueio = Column('dt_inicio_penalidade', Date, nullable=True)
    _dataTerminoImpedimentoBloqueio = Column('dt_fim_penalidade', Date, nullable=True)
    descricaoBloqueio = Column('ds_bloqueio', String(120), nullable=True)
    tipoDecisaoBloqueio = Column('tp_decisao_bloqueio', Numeric(2, 0), nullable=True)
    descricaoDecisaoBloqueio = Column('ds_decisao_bloqueio', String(22), nullable=True)
    _recolhimentoCnhBloqueada = Column('cd_recolhe_cnh', String(1), nullable=True)
    requisitosLiberacaoBloqueio = Column('ds_libera_cnh', String(30), nullable=True)
    prazoPenalBloqueio = Column('nu_prazo_penalidade', Numeric(5, 0), nullable=True)
    tipoPrazoPenalBloqueio = Column('tp_prazo_penalidade', Numeric(1, 0), nullable=True)
    _descricaoPrazoBloqueio = Column('ds_prazo_penalidade', String(3), nullable=True)
    prazoPenalTotalBloqueio = Column('nu_prazo_penalidade_total', Numeric(5, 0), nullable=True)
    _tipoPrazoTotalBloqueio = Column('tp_prazo_penalidade_total', String(1), nullable=True)
    _descricaoPrazoTotalBloqueio = Column('ds_tipo_prazo_penalidade_total', String(3), nullable=True)
    DT_MVM_DWS = Column('dt_mvm_dws', Date, nullable=True)
    DH_CRG_DWS = Column('dh_crg_dws', None, nullable=True)
    CD_VRF = Column('cd_vrf', String(32), nullable=True, primary_key=True)
    IN_EXL = Column('in_exl', Numeric(32, 0), nullable=True)

    @property
    def tipoPrazoTotalBloqueio(self):
        return int(self._tipoPrazoTotalBloqueio)

    @property
    def recolhimentoCnhBloqueada(self):
        return True if self._recolhimentoCnhBloqueada in ('1', 1, "Sim") else False

    @property
    def descricaoPrazoTotalBloqueio(self):
        return 'DIAS' if self._descricaoPrazoTotalBloqueio == 'DIA' else self._descricaoPrazoTotalBloqueio

    @property
    def descricaoPrazoBloqueio(self):
        return 'DIAS' if self._descricaoPrazoBloqueio == 'DIA' else self._descricaoPrazoBloqueioque

    @property
    def dataImpedimentoBloqueio(self):
        return retorno_data(self._dataImpedimentoBloqueio)

    @property
    def dataInicioImpedimentoBloqueio(self):
        return retorno_data(self._dataInicioImpedimentoBloqueio)

    @property
    def dataTerminoImpedimentoBloqueio(self):
        return retorno_data(self._dataTerminoImpedimentoBloqueio)

