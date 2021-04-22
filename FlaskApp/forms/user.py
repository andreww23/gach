from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Ваше имя', validators=[DataRequired()])
    about = TextAreaField("Расскажите о вашем уровне подготовки")
    submit = SubmitField('Оставить заявку')
