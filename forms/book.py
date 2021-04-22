from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class RedactorForm(FlaskForm):
    title = StringField('Название книги:')
    sinopsis = TextAreaField("Введите синопсис вашей книги (без спойлеров!):")
    text = TextAreaField("Введите сюда текст вашего произведения:")
    submit = SubmitField('Опубликовать')
