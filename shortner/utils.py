__author__ = 'Dave'

import random
import string
from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 15)

# generate random char


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new_code =''
    # for _ in range(size):
    #    new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    Klass = instance.__class__  # it is like importing models.Model import RawURL
    qs_exists = Klass.objects.filter(shortcode=new_code).exists() # checking if the shortcode exists in DB
    if qs_exists:
        return create_shortcode(size=size)  # create another shortcode
    return new_code