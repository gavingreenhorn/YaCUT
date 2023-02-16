from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    ORIGINAL_LINK_LABEL, CUSTOM_ID_LABEL, SHORT_LINK_CHAR_LIMIT,
    LONG_LINK_CHAR_LIMIT, REQUIRED_FIELD, INVALID_URL_STRING,
    INCORRECT_STRING_LENGTH, INVALID_CHARACTERS, VALID_CHARACTERS_PATTERN,
    SUBMIT_BUTTON_LABEL)


class URLMapForm(FlaskForm):
    original_link = StringField(
        label=ORIGINAL_LINK_LABEL,
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            URL(message=INVALID_URL_STRING),
            Length(
                max=LONG_LINK_CHAR_LIMIT,
                message=INCORRECT_STRING_LENGTH.format(
                    limit=LONG_LINK_CHAR_LIMIT)
            )
        ]
    )
    custom_id = StringField(
        label=CUSTOM_ID_LABEL,
        validators=[
            Length(
                max=SHORT_LINK_CHAR_LIMIT,
                message=INCORRECT_STRING_LENGTH.format(
                    limit=SHORT_LINK_CHAR_LIMIT)
            ),
            Regexp(
                regex=VALID_CHARACTERS_PATTERN,
                message=INVALID_CHARACTERS),
            Optional(strip_whitespace=True)
        ]
    )
    submit = SubmitField(SUBMIT_BUTTON_LABEL)
