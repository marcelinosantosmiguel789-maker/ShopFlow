from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Infrastructure.Database.database import Base

if TYPE_CHECKING:
    from Infrastructure.Model.itemPedidoModel import ItemPedidoModel


class PedidoModel(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    valor_total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    itens: Mapped[list["ItemPedidoModel"]] = relationship(
        back_populates="pedido"
    )