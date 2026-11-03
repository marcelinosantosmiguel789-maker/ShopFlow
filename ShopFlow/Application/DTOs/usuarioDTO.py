from pydantic import BaseModel as baseModel

from Application.DTOs.ProdutoDTO import ProdutoCreateDTO

class usuarioCreateDTO(baseModel):
    usuario: str
    senhaHash: str

