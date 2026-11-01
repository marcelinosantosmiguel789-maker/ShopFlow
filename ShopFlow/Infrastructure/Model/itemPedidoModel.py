from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Infrastructure.Database.database import Base

if TYPE_CHECKING:
    from Infrastructure.Model.pedidoModel import PedidoModel


class ItemPedidoModel(Base):
    __tablename__ = "itens_pedido"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    pedido_id: Mapped[int] = mapped_column(
        ForeignKey("pedidos.id"),
        nullable=False
    )

    produto_id: Mapped[int] = mapped_column(
        ForeignKey("produtos.id"),
        nullable=False
    )

    quantidade: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    preco_unitario: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    pedido: Mapped["PedidoModel"] = relationship(
        back_populates="itens"
    )