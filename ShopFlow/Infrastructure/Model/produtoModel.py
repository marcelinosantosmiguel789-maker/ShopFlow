from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from Infrastructure.Database.database import Base

class ProdutoModel(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(255), nullable=True)
    preco: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    estoque: Mapped[int] = mapped_column(nullable=False)
    categoriaId: Mapped[int] = mapped_column(nullable=False)