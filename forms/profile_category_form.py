from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, validators

class ProfileCategoryForm(FlaskForm):
    title = StringField(label="Enter Profile Category Title", validators=[validators.DataRequired("Required")])
    description = StringField(label="Enter Profile Category Description", validators=[validators.DataRequired("Required")])
    order = IntegerField(label="Enter Profile Category Order", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
