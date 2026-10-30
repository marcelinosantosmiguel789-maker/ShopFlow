from Domain.Repositories.produtoRepository import ProdutoRepository
from Infrastructure.Database.database import SessionLocal
from Infrastructure.Model.produtoModel import ProdutoModel


class SqlAlchemyProdutoRepository(ProdutoRepository):
    @staticmethod
    def _value(produto_data, name, default=None):
        if isinstance(produto_data, dict):
            return produto_data.get(name, default)
        return getattr(produto_data, name, default)

    @classmethod
    def _model_data(cls, produto_data):
        return {
            "nome": cls._value(produto_data, "nome"),
            "descricao": cls._value(produto_data, "descricao"),
            "preco": cls._value(produto_data, "preco"),
            "estoque": cls._value(produto_data, "estoque"),
            "categoriaId": cls._value(
                produto_data,
                "categoriaId",
                cls._value(produto_data, "categoriaID"),
            ),
        }

    def criar_produto(self, produto_data):
        session = SessionLocal()
        try:
            produto = ProdutoModel(**self._model_data(produto_data))
            session.add(produto)
            session.commit()
            session.refresh(produto)
            return produto
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def criar(self, produto_data):
        return self.criar_produto(produto_data)

    def get_by_id(self, produto_id):
        session = SessionLocal()
        try:
            return session.get(ProdutoModel, produto_id)
        finally:
            session.close()

    def create(self, produto_data):
        return self.criar_produto(produto_data)

    def update(self, produto_id, produto_data):
        session = SessionLocal()
        try:
            produto = session.get(ProdutoModel, produto_id)
            if produto is None:
                return None

            for field, value in self._model_data(produto_data).items():
                if value is not None:
                    setattr(produto, field, value)

            session.commit()
            session.refresh(produto)
            return produto
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def delete(self, produto_id):
        session = SessionLocal()
        try:
            produto = session.get(ProdutoModel, produto_id)
            if produto is None:
                return False

            session.delete(produto)
            session.commit()
            return True
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


sqlAlchemyProdutoRepository = SqlAlchemyProdutoRepository
