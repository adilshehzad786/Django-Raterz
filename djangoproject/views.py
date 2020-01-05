from django.shortcuts import render,get_object_or_404
from .models import Post,University_Program
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .filter import UserFilter
from .filter2 import UserFilter2
import json
import markdown2
import bleach
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question,Answer,Teacher_Program
from django.conf import settings
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import Http404
from .forms import ContactForm
from django.core.mail import BadHeaderError, EmailMessage
from django.db.models import Q
from django.conf import settings
from machina.apps.forum_conversation.views import TopicView as BaseTopicView
from .forms import CaptchaField,CaptchaTestForm,Add_Teacher_Form,Add_University_Form

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/index.html', context)
def index(request):
    context_index = {}
    context_index['questions'] = Question.objects.all()
    return render(request, 'djangoproject/base.html', context_index)

def faq(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request,'djangoproject/faq_page.html',context)



def askquestion(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            question = request.POST.get('question')
            posted_by = request.POST.get('posted_by')
            q = Question(question_title=title, question_text=question, posted_by=posted_by)
            q.save()
        except Exception as e:
            return render(request, 'ask_question.html', {'error': 'Something is wrong with the form!'})
    else:

        return render(request, 'djangoproject/ask_question.html', {})

def viewquestion(request, qid, qslug):
    context = {}
    question = Question.objects.get(qid=qid, slug=qslug)

    # assuming obj is a model instance
    question_json = json.loads(serializers.serialize('json', [ question ]))[0]['fields']
    question_json['date_posted'] = question.date_posted
    question_json['qid'] = question.qid
    question_json['question_text'] = bleach.clean(markdown2.markdown(question_json['question_text']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
    context['question'] = question_json
    context['answers'] = []
    answers = Answer.objects.filter(qid=qid)
    for answer in answers:
        answer.answer_text = bleach.clean(markdown2.markdown(answer.answer_text), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
        context['answers'].append(answer)
    return render(request, 'djangoproject/view-question.html', context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        if myfile.size > int(settings.MAX_UPLOAD_SIZE):
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'djangoproject/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })


    return render(request, 'djangoproject/simple_upload.html')


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(topic__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'djangoproject/search_box_2.html', context)

        else:
            return render(request, 'djangoproject/search_box_2.html')

    else:
        return render(request, 'djangoproject/search_box_2.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = DocumentForm()
    return render(request, 'djangoproject/model_form_upload.html', {
        'form': form
    })

def about(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/about.html', context)
def policies(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/privacy.html', context)

def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render(request,'users/login.html',locals())

def Skills(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/test_skills.html', context)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['muhammadadil@ucp.edu.pk'], #change to your email
                                     reply_to=[contact_email],
                                   )

                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('./thanks/')
    return render(request, 'djangoproject/contact.html', {'form': form})
def thanks(request):
    return render(request, 'djangoproject/thanks.html', {})

def thanks(request):
    return render(request, 'djangoproject/thanks.html', {})

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter2(request.GET, queryset=user_list)
    return render(request, 'djangoproject/search_box.html', {'filter': user_filter})


def search_review(request):
    context = {
        'posts': Post.objects.all()
    }
    user_filter = UserFilter(request.GET, queryset=context)
    return render(request, 'djangoproject/search_box_2.html', {'filter': user_filter})

def Team(request):
    context={
        'posts':Post.objects.all()

    }
    return render(request,'djangoproject/team.html',context)



class PostListView(ListView):
    model = Post
    template_name = 'djangoproject/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'djangoproject/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class TopicView(BaseTopicView):
  def get_context_data(self, **kwargs):
    context = super(TopicView, self).get_context_data(**kwargs)
    # Some additional data can be added to the context here
    context['foo'] = 'bar'
    return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['topic','category','content','tags','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['topic','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/education'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class NoReverseMatch(Exception):
    pass

def about(request):
    return render(request, 'djangoproject/about.html', {'title': 'About'})

#university
def University(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/university_page.html', context)

#computer_science

def ComputerScience(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/computer_science.html', context)

#Cities

def TOPCities(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/cities.html', context)

def Lahore(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/lahore.html', context)

def Pixar_rating(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'pinax/ratings/_rating.html', context)

def WhatisReview(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/whatisreview.html', context)

#donation

def Donation(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/donation.html', context)

#jazzcash
def JazzCash(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/jazzcash.html', context)


#Hacking Page

def Hacking_Page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/hacking.html', context)



#Utility

def Utility(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/utility_page.html', context)

#Wireless Hacking Page

def Wireless_Hacking(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/wireless.html', context)

#payment Method
def Payment(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/payment.html', context)

############################################################################
