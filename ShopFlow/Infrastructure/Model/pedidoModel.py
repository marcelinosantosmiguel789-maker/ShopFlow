from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from Infrastructure.Database.database import Base

class PedidoModel(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usuarioId: Mapped[int] = mapped_column(nullable=False)
    itens: Mapped[str] = mapped_column(String(255), nullable=True)
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)