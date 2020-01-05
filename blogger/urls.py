from django.contrib import admin
from django.urls import path
from blogger import views


urlpatterns = [
   path('blog/', views.blog, name='blogger_page'),
path('single_post/<post_id>/', views.single_post,  name='single_post')
]