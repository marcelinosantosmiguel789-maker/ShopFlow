from abc import ABC, abstractmethod

class pedidoRepository(ABC):
    @abstractmethod
    def criar_pedido(self, pedido):
        pass

    @abstractmethod
    def obter_pedido_por_id(self, pedido_id):
        pass

    @abstractmethod
    def atualizar_pedido(self, pedido):
        pass

    @abstractmethod
    def deletar_pedido(self, pedido_id):
        pass