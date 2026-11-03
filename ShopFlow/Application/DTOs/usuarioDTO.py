from pydantic import BaseModel as baseModel

from Application.DTOs.ProdutoDTO import ProdutoCreateDTO

class usuarioCreateDTO(baseModel):
    id: int
    usuario: str
    senhaHash: str

