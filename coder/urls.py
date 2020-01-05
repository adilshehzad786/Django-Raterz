
from django.urls import path
from coder.views.question import QuestionHomePage, QuestionCreate, QuestionRedirectView

from coder.views import question

urlpatterns = [

path('main/',question.index, name='coding_help'),
path('homepage/',QuestionHomePage.as_view(),name='questionhomepage'),
path('homepage/create/', QuestionCreate.as_view(),
        name='question_create'),
path('homepage/<int:pk>',
        QuestionRedirectView.as_view(),
        name='question_redirect')


]