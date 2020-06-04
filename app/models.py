from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json

def upload_updated_image(instance, filename):
    return f'updates/{instance.user}/{filename}'

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        return serialize("json", qs , fields=['user','content','image'])
    def serialize1(self):
        qs = self
        final_array = []
        for obj in qs:
            stuct = json.loads(obj.serialize1())
            final_array.append(stuct)
        return json.dumps(final_array)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model,using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=upload_updated_image, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""
    def serialize(self):
        return serialize("json",[self,],fields=('user','content','image'))

    def serialize1(self):
        json_data = serialize("json", [self,])
        stuct = json.loads(json_data)
        print(stuct)
        data = json.dumps(stuct[0]['fields'])
        return data