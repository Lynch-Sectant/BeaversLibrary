import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlachemy import orm


class Book(SqlAlchemyBase):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    author_rel = orm.relation('User')
    sinopsis = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    text = sqlalchemy.Column(sqlalchemy.Text, unique=True, nullable=True)
    tag_from_length = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tag = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    rate = sqlalchemy.Column(sqlalchemy.Float, default=5.0)
