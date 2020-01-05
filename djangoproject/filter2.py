from .models import Post,File_Document
from simple_search import search_form_factory
import django_filters

from django import forms

class UserFilter2(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['topic']


