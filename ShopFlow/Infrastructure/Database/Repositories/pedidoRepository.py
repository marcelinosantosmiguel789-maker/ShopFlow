from Domain.Repositories.pedidoRepository import pedidoRepository
from Infrastructure.Database.database import SessionLocal
from Infrastructure.Model.pedidoModel import PedidoModel

class sqlAlchemyPedidoRepository(pedidoRepository):
    @staticmethod
    def _value(pedido_data, name, default=None):
        if isinstance(pedido_data,dict):
            return pedido_data.get(name, default)
        return getattr(pedido_data, name, default)