__author__ = 'Dave'

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator()
    reg_value = value
    if 'http' in reg_value:
        new_value = reg_value
    else:
        new_value = 'http://'+ reg_value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Iyo URL wapi")
    return new_value


def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("There is no .com in your url")
