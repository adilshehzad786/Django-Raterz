from django.db import models
from froala_editor.fields import FroalaField





class Course_Category(models.Model):
    course_name=models.CharField(max_length=50)
    course_slug=models.SlugField(max_length=50,unique=True,help_text='Unique Value For Product Page Url,Created From Name.')
    course_description=models.TextField()
    course_is_active=models.BooleanField(default=True)




class Courses(models.Model):
    Course_name=models.CharField(max_length=100)
    descriptions= FroalaField(options={
        'toolbarInline': True,
    })
    is_active=models.BooleanField(default=False)
    course_link=models.URLField(max_length=300,db_index=True,
        unique=True,
        blank=True)
    promo_code=models.CharField(max_length=50)
    course_meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                            help_text='comma-delimited set of SEO keywords for meta Tag')
    course_created_at = models.DateTimeField(auto_now_add=True)
    course_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Course_name
