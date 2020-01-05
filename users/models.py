from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from simple_history.models import HistoricalRecords
from djangoproject.custom_azure import AzureMediaStorage as AMS
from django.core.exceptions import ValidationError
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics',null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def clean_avatar(self):
        image=self.cleaned_data.get("image_file")

        if image:
            print (image.size)
            if image.size > 1000000:
                raise ValidationError("File is too big")
            image = Image.open(image)
            #image = MakeThumbnail(image)
            return image
        else:
            raise ValidationError("File is corrupted")

