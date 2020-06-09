from django.db import models
from django.conf import settings


def upload_status_image(instance,filename):
    return f'updates/{instance.user.id}/{filename}'


class StatusQueryset(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQueryset(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.id) +str(self.content)[:50]

    class Meta:
        verbose_name = 'Status Post'
        verbose_name_plural = 'Status Posts'