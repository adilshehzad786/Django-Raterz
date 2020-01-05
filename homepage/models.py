from django.db import models
from taggit.managers import TaggableManager
class Seo(models.Model):
    tagger=TaggableManager()

