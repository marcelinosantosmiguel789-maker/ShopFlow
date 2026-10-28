from abc import ABC, abstractmethod

class ProdutoRepository(ABC):
    @abstractmethod
    def criar_produto(self, produto_data):
        pass

    @abstractmethod
    def get_by_id(self, produto_id):
        pass

    @abstractmethod
    def create(self, produto_data):
        pass

    @abstractmethod
    def update(self, produto_id, produto_data):
        pass

    @abstractmethod
    def delete(self, produto_id):
        pass