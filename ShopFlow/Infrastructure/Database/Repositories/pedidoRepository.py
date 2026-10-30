from Domain.Repositories.pedidoRepository import pedidoRepository
from Infrastructure.Database.database import SessionLocal
from Infrastructure.Model.pedidoModel import PedidoModel

class SqlAlchemyPedidoRepository(pedidoRepository):
    @staticmethod
    def _value(pedido_data, name, default=None):
        if isinstance(pedido_data,dict):
            return pedido_data.get(name, default)
        return getattr(pedido_data, name, default)
    @classmethod
    def _model_data(cls, pedido_data):
        return{
            "id": cls._value(pedido_data, "id"),
            "usuario_id":cls._value(pedido_data, "usuario_id"),
            "status":cls._value(pedido_data, "status"),
            "data_criacao":cls._value(pedido_data, "data_criacao")
        }