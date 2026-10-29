from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from Infrastructure.Database.database import Base

class itemPedidoModel(Base):
    __tablename__ = "itemPedido"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    pedidoId: Mapped[int] = mapped_column(nullable=False)
    produtoId: Mapped[int] = mapped_column(nullable=False)
    quantidade: Mapped[int] = mapped_column(nullable=False)
    precoUnitario: Mapped[float] = mapped_column(nullable=False)


