from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render, redirect
from coder.models.question import Question,QuestionSuggestedEdits
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,DetailView
from coder.forms.question import QuestionForm
from coder.forms.question import QuestionSuggestedEditsForm
from reversion_compare.views import HistoryCompareDetailView
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from reversion.views import RevisionMixin

@login_required
def index(request):
    if request.method == 'POST':
        messages.success(request, f'Login Successfully ')
        return redirect('questionhomepage')


    return render(request, 'question_homepage.html')


class QuestionHomePage(ListView):
    model = Question
    context_object_name = 'questions'

    template_name = 'question_homepage.html'


class QuestionRedirectView(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['pk'])
        return reverse('question_detail', kwargs={'pk': question.pk, 'slug': question.slug})


class QuestionDetail(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'question_detail.html'




class QuestionCreate(LoginRequiredMixin, FormView):
    template_name = 'question_create.html'
    form_class = QuestionForm

    def form_valid(self, form):
        initial = form.save(commit=False)
        initial.author = self.request.user
        initial.save()
        form.save_m2m()
        messages.success(self.request,('Question successfully created!'))
        return redirect(reverse('question_redirect', kwargs={'pk': initial.pk}))

class QuestionSuggestedEditsCreate(LoginRequiredMixin,RevisionMixin,FormView):

    template_name = 'question_suggested_edits_create.html'
    form_class = QuestionSuggestedEditsForm
    model = QuestionSuggestedEdits

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs['pk'])

    def form_valid(self, form):
        # updating the last editor
        question = self.get_object()
        question.editor = self.request.user
        question.edited = True
        question.save()

        initial = form.save(commit=False)
        initial.question = question
        initial.editor = self.request.user

        # automate status=approved if it is owned.
        if question.author == question.editor:
            initial.status == 'approved'

        initial.save()
        form.save_m2m()

        messages.success(self.request,('Edit suggestion successfully created!'))
        return redirect(reverse('question_redirect', kwargs={'pk': self.get_object().pk}))

    def get_initial(self):
        initial = super(QuestionSuggestedEditsCreate, self).get_initial()
        for field, _cls in self.form_class.base_fields.items():
            if field == 'tags':
                value = self.get_object().tags.all()
            elif field == 'comment':
                value = ''
            else:
                value = getattr(self.get_object(), field)
            initial.update({field: value})
        return initial

    def get_context_data(self, **kwargs):
        context = super(QuestionSuggestedEditsCreate, self).get_context_data(**kwargs)
        context['question'] = self.get_object()
        return context


class QuestionSuggestedEditsReversions(HistoryCompareDetailView):
    template_name = 'question_revisions.html'
    context_object_name = 'question_suggested_edits'
    model = QuestionSuggestedEdits
    compare_fields = ('description', )

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

