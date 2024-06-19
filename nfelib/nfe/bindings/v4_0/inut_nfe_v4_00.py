"""This file was generated by xsdata, v24.2.1, on 2024-06-19 02:16:35

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass
from nfelib.nfe.bindings.v4_0.leiaute_inut_nfe_v4_00 import TinutNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class InutNfe(TinutNfe):
    """
    Schema XML de validação do Pedido de Inutilização de Numeração da Nota Fiscal
    Eletrônica.
    """

    class Meta:
        name = "inutNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
