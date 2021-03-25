import sqlalchemy
from .db_session import SqlAlchemyBase


class Book(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("authors.id"))
    author = orm.relation('Author')
    tag_from_length = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tag = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    text = sqlalchemy.Column(sqlalchemy.String)
