from django.contrib import admin
from .models import Answer,Equation
# Register your models here.

class EquationInline(admin.TabularInline):
    model = Equation
    extra = 1

class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Answer',               {'fields': ['answer_value']}),

    ]
    inlines = [EquationInline]

admin.site.register(Answer,AnswerAdmin)