from django.contrib import admin

from .models import Question_Choice,Category_Choice

admin.site.register(Question_Choice)
admin.site.register(Category_Choice)