from flask_WTF import FlaskForm

from wtforms import StringField, SubmitField, IntgerField #importing classes
#background blueprint for our form
class newAnimalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    weight = IntegerField('Weight')
    height = IntegerField('Height')
    climate = StringField('Climate')
    region = StringField('Region')
    submit_button = SubmitField()
