from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from Infrastructure.Database.database import Base

class usuarioModel(Base):
    __tablename__ = "Usuario"
    nome: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    senhaHash: Mapped[str] = mapped_column(nullable=False)