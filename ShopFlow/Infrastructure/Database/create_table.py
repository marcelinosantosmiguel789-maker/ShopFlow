from Infrastructure.Database.database import Base, engine

from Infrastructure.Model.carrinhoModel import CarrinhoModel
from Infrastructure.Model.categoriaModel import CategoriaModel
from Infrastructure.Model.itemPedidoModel import itemPedidoModel
from Infrastructure.Model.pedidoModel import PedidoModel
from Infrastructure.Model.produtoModel import ProdutoModel
from Infrastructure.Model.usuarioModel import usuarioModel

def criar_tabelas() -> None:
        Base.metadata.create_all(bind=engine)
        print("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    criar_tabelas()