from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from Infrastructure.Database.database import Base

class PedidoModel(Base):
    __tablename__ = "pedidos"

    usuarioId: Mapped[int] = mapped_column(nullable=False)
    itens: Mapped[str] = mapped_column(String(255), nullable=True)