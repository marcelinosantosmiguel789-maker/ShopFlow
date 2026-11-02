from pydantic import BaseModel as baseModel


class ProdutoCreateDTO(baseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade: int
