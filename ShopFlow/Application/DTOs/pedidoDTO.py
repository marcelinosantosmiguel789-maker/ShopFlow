from pydantic import BaseModel as baseModel

from Application.DTOs.ProdutoDTO import ProdutoCreateDTO

class PedidoDTO(baseModel):
    usuario_id: int
    produtos: list[ProdutoCreateDTO]
    total: float
    status: str