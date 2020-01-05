from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin


class QuestionAdmin(CompareVersionAdmin):
    pass

class QuestionSuggestion(CompareVersionAdmin):
    pass