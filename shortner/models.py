from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
# from django_hosts.resolvers import reverse

from .utils import create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX",
                        15)  # check in settings if there is SHORTCODE_MAX, if there isn't set it to 15


# A model manager
class RawURLManager(models.Model):
    def all(self, *args, **kwargs):
        qs_main = super(RawURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcode(self):
        qs = RawURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made {i}".format(i=new_codes)


# Create your models here.
class RawURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # when model was updated
    timestamp = models.DateTimeField(auto_now_add=True)  # when model was created
    active = models.BooleanField(default=True)  # active or not

    m = RawURLManager()  # to make this model manager active, we can use m.objects.all() to check the unactive ones

    # overriding save method
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)  # immediately generate shortcode when they are blank only
        super(RawURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, )
        # 'calt.bay/{shortcode}'.format(shortcode=self.shortcode)
        return 'calt.bay' + url_path

# python manage.py makemigrations
# python manage.py migrate
