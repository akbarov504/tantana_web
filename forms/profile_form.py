from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, validators, TextAreaField
from flask_wtf.file import FileField

class ProfileForm(FlaskForm):
    title = StringField(label="Enter Profile Title", validators=[validators.DataRequired("Required")])
    category = SelectField(label="Select Profile Category", validators=[validators.DataRequired("Required")])
    respublika = SelectField(label="Select Profile Respublika", validators=[validators.DataRequired("Required")])
    viloyat = SelectField(label="Select Profile Viloyat", validators=[validators.DataRequired("Required")])
    tuman = SelectField(label="Select Profile Tuman", validators=[validators.DataRequired("Required")])
    street = StringField(label="Select Profile Street", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")

class ProfileImageForm(FlaskForm):
    image = FileField(label="Enter Profile Image")
    img1 = FileField(label="Enter Profile Image")
    img2 = FileField(label="Enter Profile Image")
    img3 = FileField(label="Enter Profile Image")
    img4 = FileField(label="Enter Profile Image")
    img5 = FileField(label="Enter Profile Image")
    img6 = FileField(label="Enter Profile Image")
    img7 = FileField(label="Enter Profile Image")
    img8 = FileField(label="Enter Profile Image")
    img9 = FileField(label="Enter Profile Image")
    img10 = FileField(label="Enter Profile Image")
    description = TextAreaField(label="Enter Profile Description")
    submit = SubmitField(label="Edit")
