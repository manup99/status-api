from django.db import models
from django.conf import settings

def upload_updated_image(instance, filename):
    return f'updates/{instance.user}/{filename}'
class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=upload_updated_image, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content or ""
