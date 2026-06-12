from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Medication(Base):
    __tablename__ = "medications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False,
        unique=True
    )

    stock = Column(
        Integer,
        nullable=False,
        default=0
    )

    price = Column(
        Float,
        nullable=False
    )