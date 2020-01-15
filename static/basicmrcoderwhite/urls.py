from django.urls import path

from basicmrcoderwhite.views import mrcoder_question
from basicmrcoderwhite.views.mrcoder_question import QuestionCreateViewer,QuestionDetailViewer,IndexViewer

urlpatterns = [
    path('home/', mrcoder_question.index, name='whitehomepage'),
    path('myhome', IndexViewer.as_view(), name='myhome'),
    path('create_new', QuestionCreateViewer.as_view(), name='create_question2'),
    path('<slug:slug>$', QuestionDetailViewer.as_view(), name='question2'),



]