from reversion_compare.admin import CompareVersionAdmin
from django.contrib import admin
from coder.models.question import Question
admin.site.register(Question)

class Comment(CompareVersionAdmin):
    pass