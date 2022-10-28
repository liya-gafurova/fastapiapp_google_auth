from sqlalchemy import String, Column, Text, DateTime, sql

from db.db import Base


class Post(Base):
    id = Column(String(50), primary_key=True)

    title = Column(String(200))
    text = Column(Text, nullable=False)

    created = Column(DateTime(timezone=True), server_default=sql.func.now())