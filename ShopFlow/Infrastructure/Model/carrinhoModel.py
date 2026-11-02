from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Infrastructure.Database.database import Base

if TYPE_CHECKING:
    from Infrastructure.Model.itemCarrinhoModel import ItemCarrinhoModel


class CarrinhoModel(Base):
    __tablename__ = "carrinhos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False,
        unique=True
    )
    itens: Mapped[list["ItemCarrinhoModel"]] = relationship(
        back_populates="carrinho",
        cascade="all, delete-orphan",
    )