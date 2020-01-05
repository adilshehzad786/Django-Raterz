from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
from django.db.models.signals import post_save

from django.core.exceptions import ValidationError
from PIL import Image
STATUS = (
    (0, 'No Progress'),
    (1, 'Approved'),
    (2, 'Rejected'),
)

DAYS = (
    [(i, i) for i in range(1, 31)]
)

MONTHS = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
)


YEARS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5,'5'),
        (6,'6'),
    )

SEMESTER = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),

)

LEVELS = (
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
)

TYPES = (
    ('o', 'Madatory'),
    ('z', 'election'),
)


class Program(models.Model):
    name = models.CharField(max_length=150)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=600, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    credits = models.IntegerField(null=True, default=0)
    Madatory = models.BooleanField(default=True)
    year = models.IntegerField(choices=YEARS, default=1)
    semester = models.IntegerField(choices=SEMESTER, default=1)
    level = models.CharField(max_length=100, choices=LEVELS, default='Bachelor')

    def __str__(self):
        return self.name

    def get_type(self):
        if self.Madatory:
            return "O"
        else:
            return "Z"


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    picture = models.ImageField(null=True, blank=True, default='no-img.png')
    website = models.URLField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, null=True)
    course = models.ManyToManyField(Course, related_name='course', blank=True)
    course_teacher = models.ManyToManyField(Course, related_name='course_teacher', blank=True)
    year = models.IntegerField(choices=YEARS, default=1)
    semester = models.IntegerField(choices=SEMESTER, default=1)
    level = models.CharField(max_length=100, choices=LEVELS, default=1)


    def get_website(self):
        if self.website[0:4] != 'http':
            return 'http://' + self.website
        else:
            return self.website

    def __str__(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return 'Student'


def create_profile(sender, **kwargs):
    if kwargs['created']:
        student = Student.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class New(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    picture = models.ImageField(null=True, blank=True,upload_to='\profile_pics')
    create_date = models.DateTimeField(default=datetime.now)

    def get_content(self):
        return self.content[:150] + '...'

    def __str__(self):
        return self.title



class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return self.student.student.first_name + ' ' + self.student.student.last_name


class Upload(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='profile_pics',null=True, validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])])
    upload_time = models.DateTimeField(default=datetime.now, null=True)
    course_link = models.URLField(max_length=300, db_index=True,
                                  unique=True,
                                  blank=True)
    def get_extension_short(self):
        ext = str(self.file).split(".")
        ext = ext[len(ext)-1]

        if ext == 'doc' or ext == 'docx':
            return 'word'
        elif ext == 'pdf':
            return 'pdf'



    def __str__(self):
        return str(self.file)[6:]

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


def get_full_name(self):
    if self.student.first_name and self.student.last_name:
        return self.student.first_name + ' ' + self.student.last_name
    return self.username




