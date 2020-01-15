from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from basicmrcoderwhite.models import Category_Choice,Question_Choice
from django.db.models import Count, Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from basicmrcoderwhite.forms import PostForm
from basicmrcoderwhite.filter import questions_filter
@login_required
def index(request):
    if request.method == 'POST':
        messages.success(request, f'Login Successfully ')
        return redirect('whitehomepage')


    return render(request, 'base_white.html')

class IndexViewer(generic.ListView):
    template_name = 'index_page.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return questions_filter(self.request, Question_Choice)


class QuestionDetailViewer(generic.DetailView):
    model = Question_Choice
    template_name = 'question_detail_get.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm

        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.creator = request.user
            reply.question = self.get_object()
            reply.save()

            self.object = self.get_object()

            context = context = super().get_context_data(**kwargs)
            context['form'] = PostForm

            messages.success(
                self.request, 'Your reply is successfully submitted!')

            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form

            return self.render_to_response(context=context)




class QuestionCreateViewer(LoginRequiredMixin, generic.CreateView):
    login_url = '/login'
    model = Question_Choice
    template_name = 'create_question.html'
    fields = ['mrcoder_category', 'mrcoder_title', 'mrcoder_content']

    def form_valid_check(self, form):
        form.instance.owner = self.request.user
        messages.success(
            self.request, 'Your questions is successfully submitted!')
        return super().form_valid_check(form)

