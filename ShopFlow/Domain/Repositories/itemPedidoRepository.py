from abc import ABC, abstractmethod

class itemPedidoRepository(ABC):
    @abstractmethod
    def criar_item_pedido(self, item_pedido):
        pass

    @abstractmethod
    def obter_item_pedido_por_id(self, item_pedido_id):
        pass

    @abstractmethod
    def atualizar_item_pedido(self, item_pedido):
        pass

    @abstractmethod
    def deletar_item_pedido(self, item_pedido_id):
        pass