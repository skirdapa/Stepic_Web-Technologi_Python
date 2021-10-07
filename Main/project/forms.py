from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, Length, InputRequired


class MessageForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email("!!!", granular_message=True)])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


class ProfileForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[Length(min=5, max=32), InputRequired()])
    password = PasswordField("Пароль", validators=[Length(min=9, max=24), InputRequired()])
    about_me = TextAreaField("О себе", validators=[])
    submit = SubmitField("Принять")
