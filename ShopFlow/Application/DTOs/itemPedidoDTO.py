from pydantic import BaseModel as baseModel
from Application.DTOs.ProdutoDTO import ProdutoCreateDTO
from Application.DTOs.pedidoDTO import PedidoDTO

class itemPedidoDTO(baseModel):
    pedido_id: list[PedidoDTO]
    produto_id: list[ProdutoCreateDTO]
    quantidade: int
    precoUnitario: float
