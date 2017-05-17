from django.db import models
from shortner.models import RawURL


# Create your models here.
class ClickEventManager(models.Model):
    def createEvent(self, RawInstance):
        if isinstance(RawInstance, RawURL):
            obj, created = self.get_or_create(url=RawInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class Click_Event(models.Model):
    raw_url = models.OneToOneField(RawURL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return '{i}'.format(i=self.count)
