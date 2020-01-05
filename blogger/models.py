from django.db import models

from django.db import models
from froala_editor.fields import FroalaField
from django.core.exceptions import ValidationError
from PIL import Image
class Article(models.Model):
   title = models.CharField(max_length=120)
   content = FroalaField(options={
      'toolbarInline': True,
   })
   updated = models.DateTimeField(auto_now=True)
   timestamp = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.title

   def clean_avatar(self):
      image = self.cleaned_data.get("image_file")

      if image:
         print(image.size)
         if image.size > 1000000:
            raise ValidationError("File is too big")
         image = Image.open(image)
         # image = MakeThumbnail(image)
         return image
      else:
         raise ValidationError("File is corrupted")