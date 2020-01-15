from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from martor.models import MartorField

class Category_Choice(models.Model):
    mrcoder_title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, editable=False)
    mrcoder_description =models.CharField(max_length=300)
    mrcoder_created_at = models.DateTimeField(auto_now_add=True)
    mrcoder_updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child',on_delete=models.CASCADE)

    def __str__(self):
        return self.mrcoder_title



    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.mrcoder_title)

        super().save(*args, **kwargs)



class Question_Choice(models.Model):
    mrcoder_category = models.ForeignKey(
        Category_Choice, on_delete=models.CASCADE,related_name='mrcoder_question')
    mrcoder_owner = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='mrcoder_question',null=True)
    mrcoder_title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, editable=False)
    mrcoder_content =MartorField(null=True)
    mrcoder_created_at = models.DateTimeField(auto_now_add=True)
    mrcoder_updated_at = models.DateTimeField(auto_now=True)
    mrcoder_solved = models.BooleanField(default=False)


    def __str__(self):
        return self.mrcoder_title

    def get_absolute_url(self):
        return reverse('question2', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.mrcoder_title)

        super().save(*args, **kwargs)


