from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField("Имя", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    birthdate = DateField("Дата рождения")
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired(),
            Length(min=8),
            Regexp(regex=r"\d[0-9a-zA-Za-яА-я]"),
        ],
    )
    confirm_password = PasswordField(
        "Подтверждение пароля", validators=[DataRequired(), EqualTo("password")]
    )
    personal_data = BooleanField(
        "Согласие на обработку персональных данных", validators=[DataRequired()]
    )
