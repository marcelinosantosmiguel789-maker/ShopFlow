from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Infrastructure.Database.database import Base

if TYPE_CHECKING:
    from Infrastructure.Model.carrinhoModel import CarrinhoModel
    from Infrastructure.Model.produtoModel import ProdutoModel


class ItemCarrinhoModel(Base):
    __tablename__ = "itens_carrinho"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    carrinho_id: Mapped[int] = mapped_column(
        ForeignKey("carrinhos.id"),
        nullable=False,
    )
    produto_id: Mapped[int] = mapped_column(
        ForeignKey("produtos.id"),
        nullable=False,
    )
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)

    carrinho: Mapped["CarrinhoModel"] = relationship(
        back_populates="itens",
    )
    produto: Mapped["ProdutoModel"] = relationship()
