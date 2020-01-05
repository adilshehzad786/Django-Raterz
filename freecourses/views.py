from django.shortcuts import render
from .models import Courses
def Index(request):
  all_post = Courses.objects.all()
  context = {
  'all_post': all_post
  }
  return render(request, 'djangoproject/freecourse.html', context)


def Post_page(request, post_id):
  posts = Courses.objects.get(pk=post_id)
  return render(request, 'djangoproject/post_page.html', {'posts': posts})
