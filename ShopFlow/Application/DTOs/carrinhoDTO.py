from pydantic import BaseModel as baseModel

from Application.DTOs.ProdutoDTO import ProdutoCreateDTO


class CarrinhoCreateDTO(baseModel):
    id: int
    produtos: list[ProdutoCreateDTO]


