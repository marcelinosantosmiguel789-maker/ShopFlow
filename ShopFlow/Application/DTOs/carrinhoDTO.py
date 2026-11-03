from pydantic import BaseModel as baseModel

from Application.DTOs.ProdutoDTO import ProdutoCreateDTO


class CarrinhoCreateDTO(baseModel):
    produtos: list[ProdutoCreateDTO]


