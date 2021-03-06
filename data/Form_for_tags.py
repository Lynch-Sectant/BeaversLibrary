import sqlalchemy
from .db_session import SqlAlchemyBase


class Tag(SqlAlchemyBase):
    __tablename__ = 'tags'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
