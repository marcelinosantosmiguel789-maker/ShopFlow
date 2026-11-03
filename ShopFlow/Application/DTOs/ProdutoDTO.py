from unicodedata import decimal

from pydantic import BaseModel as baseModel


class ProdutoCreateDTO(baseModel):
    nome: str
    descricao: str
    preco: decimal.Decimal
    estoque: int

