from abc import ABC, abstractmethod

class carrinhoRepository(ABC):
    @abstractmethod
    def criar_carrinho(self, carrinho):
        pass

    @abstractmethod
    def obter_carrinho_por_usuario_id(self, usuario_id):
        pass

    @abstractmethod
    def atualizar_carrinho(self, carrinho):
        pass

    @abstractmethod
    def deletar_carrinho(self, usuario_id):
        pass