from Domain.Repositories.pedidoRepository import pedidoRepository
from Infrastructure.Database.database import SessionLocal
from Infrastructure.Model.pedidoModel import PedidoModel

class sqlAlchemyPedidoRepository(pedidoRepository):
    @staticmethod
    def _value(produto)