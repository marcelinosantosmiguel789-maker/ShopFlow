from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Numeric, String

from Infrastructure.Database.database import Base

class CarrinhoModel(Base):
    __tablename__ = "carrinhos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usuarioId: Mapped[int] = mapped_column(ForeignKey("usuario_Id"))
    itens: Mapped[str] = mapped_column(String(255), nullable=True)