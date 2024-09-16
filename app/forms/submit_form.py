from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional

class SubmitForm(FlaskForm):
    tool_name = StringField('Tool Name', validators=[DataRequired()])
    tool_link = StringField('Tool Link', validators=[DataRequired(), URL()])
    product_hunt_link = StringField('Product Hunt Link', validators=[Optional(), URL()])
    tool_categories = StringField('Tool Categories', validators=[DataRequired()])
    tool_description = TextAreaField('Tool Description', validators=[DataRequired()])
    tool_tags = StringField('Tool Tags', validators=[DataRequired()])
    submit = SubmitField('Submit')
