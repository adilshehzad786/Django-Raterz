
from django.urls import path
from freecourses import views


urlpatterns = [
path('courses/',views.Index,name='course_page'),
path('post_page/<post_id>/', views.Post_page,  name='post_page'),

]