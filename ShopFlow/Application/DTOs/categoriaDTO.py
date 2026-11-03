from pydantic import BaseModel as baseModel

from Application.DTOs.ProdutoDTO import ProdutoCreateDTO

class CategoriaCreateDTO(baseModel):
    nome: str
    descricao: str
