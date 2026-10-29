from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from Infrastructure.Database.database import Base

class CategoriaModel(Base):
    __tablename__ = "categorias"

    nome: Mapped[str] = mapped_column(String(100), primary_key=True, nullable=False)
    descricao: Mapped[str] = mapped_column(String(255), nullable=True)
