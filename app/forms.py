from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length,InputRequired, Email
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
  
    name = StringField('Name',validators=[DataRequired()])
    #email = StringField('Email',validators=[DataRequired()])
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
    subject = StringField('Subject',validators=[DataRequired(), Length(max=10)])

    #body = TextField('Message',validators=[DataRequired()])
    body = TextAreaField('Message', [
        DataRequired()
        ])
   # submit = SubmitField("Send")
     

