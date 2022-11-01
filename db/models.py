from sqlalchemy import String, Column, Text, DateTime, sql, Boolean

from db.db import Base


class Post(Base):
    id = Column(String(50), primary_key=True)

    title = Column(String(200))
    text = Column(Text, nullable=False)

    created = Column(DateTime(timezone=True), server_default=sql.func.now())


class User(Base):
    id = Column(String, primary_key=True)

    username = Column(String(50), nullable = False)
    full_name = Column(String(100))
    email = Column(String(50), unique=True)

    created = Column(DateTime(timezone=True), server_default=sql.func.now())

    is_active = Column(Boolean, server_default=sql.expression.true())

