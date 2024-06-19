"""This file was generated by xsdata, v24.2.1, on 2024-06-19 02:16:35

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass
from nfelib.nfe.bindings.v4_0.leiaute_cons_stat_serv_v4_00 import (
    TretConsStatServ,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetConsStatServ(TretConsStatServ):
    """
    Schema XML de validação do Resultado da Consulta do Status do Serviço.
    """

    class Meta:
        name = "retConsStatServ"
        namespace = "http://www.portalfiscal.inf.br/nfe"
