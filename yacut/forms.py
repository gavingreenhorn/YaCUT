from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    ORIGINAL_LINK_LABEL, CUSTOM_ID_LABEL, SHORT_LINK_CHAR_LIMIT,
    REQUIRED_FIELD_MSG, INVALID_URL_STRING_MSG, INCORRECT_STRING_LENGTH_MSG,
    INVALID_CHARACTERS_MSG)


class URLMapForm(FlaskForm):
    original_link = StringField(
        label=ORIGINAL_LINK_LABEL,
        validators=[
            DataRequired(message=REQUIRED_FIELD_MSG),
            URL(message=INVALID_URL_STRING_MSG)
        ]
    )
    custom_id = StringField(
        label=CUSTOM_ID_LABEL,
        validators=[
            Length(
                min=1,
                max=SHORT_LINK_CHAR_LIMIT,
                message=INCORRECT_STRING_LENGTH_MSG.format(
                    limit=SHORT_LINK_CHAR_LIMIT)),
            Regexp(
                regex=r'^[a-zA-Z\d]*$',
                message=INVALID_CHARACTERS_MSG),
            Optional(strip_whitespace=True)
        ]
    )
    submit = SubmitField('Создать')
