from django.shortcuts import render
from .models import Article
# Create your views here.
def blog(request):
  all_post = Article.objects.all()
  context = {
  'all_post': all_post
  }
  return render(request, 'djangoproject/blog.html', context)


def single_post(request, post_id):
  post = Article.objects.get(pk=post_id)
  return render(request, 'djangoproject/single_post.html', {'post': post})