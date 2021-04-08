from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    text = StringField('Текст', validators=[DataRequired()])
    submit = SubmitField('Войти')
