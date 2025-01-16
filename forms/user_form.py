from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, SelectField, PasswordField, validators

class LoginForm(FlaskForm):
    phone = StringField(label="Телефон рақамингизни киритинг", validators=[validators.Length(min=13, max=13), validators.DataRequired("Required"), validators.Regexp("^\+998(50|99|97|98|95|20|93|94|33|55|61|62|65|66|67|69|70|71|72|73|74|75|76|77|78|79|88|90|91)(\d{7})$")])
    password = PasswordField(label="Паролингизни киритинг", validators=[validators.Length(min=8, max=300), validators.DataRequired("Required")])
    submit = SubmitField(label="Кириш")

class RegisterForm(FlaskForm):
    first_name = StringField(label="Исмингиз", validators=[validators.Length(min=3, max=300), validators.DataRequired("Required")])
    last_name = StringField(label="Фамилиянгиз", validators=[validators.Length(min=3, max=300), validators.DataRequired("Required")])
    phone = StringField(label="Телефон рақамингизни киритинг", validators=[validators.Length(min=13, max=13), validators.DataRequired("Required"), validators.Regexp("^\+998(50|99|97|98|95|20|93|94|33|55|61|62|65|66|67|69|70|71|72|73|74|75|76|77|78|79|88|90|91)(\d{7})$")])
    type = RadioField(label="Ким сифатида кирмоқчисиз?", validators=[validators.DataRequired("Required")], choices=["Мижоз", "Сервис қўшиш учун"])
    password = PasswordField(label="Паролингизни киритинг", validators=[validators.Length(min=8, max=300), validators.DataRequired("Required")])
    submit = SubmitField(label="Рўйхатдан ўтиш")
