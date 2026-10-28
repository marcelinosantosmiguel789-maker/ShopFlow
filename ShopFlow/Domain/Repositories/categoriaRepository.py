from abc import ABC, abstractmethod

class categoriaRepository(ABC):
    @abstractmethod
    def criar_categoria(self, categoria):
        pass

    @abstractmethod
    def obter_categoria_por_id(self, categoria_id):
        pass

    @abstractmethod
    def atualizar_categoria(self, categoria):
        pass

    @abstractmethod
    def deletar_categoria(self, categoria_id):
        pass