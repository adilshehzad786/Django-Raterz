from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
from simple_history.models import HistoricalRecords
from machina.apps.forum_conversation.abstract_models import AbstractTopic
from taggit.managers import TaggableManager
from froala_editor.fields import FroalaField
class Teacher_Program(models.Model):
    name = models.CharField(max_length=150)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class University_Program(models.Model):
    name = models.CharField(max_length=150)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Admin_instructor_Add(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name


class Post(models.Model):
    Fun='Fun'
    Knowledge='Knowledge'
    Science='Science'
    TYPES = (
        (Fun, 'Fun'),
        (Knowledge, 'Knowledge'),
        (Science, 'Science'),
    )

    topic=models.CharField(max_length=50)
    category=models.CharField(choices=TYPES,max_length=50,default=Knowledge)
    content=FroalaField(help_text="ignore Message From Froala")
    image=models.ImageField(blank=False,null=False,upload_to='profile_pics',default='default.jpg')

    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1,related_name='%(class)s_requests_created')

    tags = TaggableManager(help_text="Write Tags Relevant With Your Post E.g facebook,google,amazon . Tags Help in Boosting Posting SEO")
    course_meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                            help_text='comma-delimited set of SEO keywords for meta Tag')
    def __str__(self):
        return self.instructor

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=100)
    question_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        def __init__(self, *args, **kwargs):
            super(Question, self).__init__(*args, **kwargs)


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)


class File_Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file_document = models.FileField(upload_to='documents/%Y/%m/%d/',max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Topic(AbstractTopic):
    icon = models.ImageField(verbose_name="Icon", upload_to="forum/topic_icons")

