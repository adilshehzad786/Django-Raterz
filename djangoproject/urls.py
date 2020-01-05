from django.contrib import admin
from django.urls import path,include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    UserFilter,


)
from django_filters.views import FilterView
from django import urls
from . import views
from django.conf.urls import url

urlpatterns = [

    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),

    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('news/',PostListView.as_view(),name='news'),
    path('about/',views.about,name='blog-about'),
    path('team/',views.Team,name='team'),
    path('test_skills',views.Skills,name='test_skills'),
    path(r'search/',FilterView.as_view(filterset_class=UserFilter,template_name='djangoproject/search_box.html'),name='search-blog'),
    path(r'search_review/',views.searchposts,name='search-blog-review'),
    path(r'ask_question/',views.askquestion,name='ask-question'),
    path(r'view_question/<int:qid>/<slug:qslug>', views.viewquestion,name='view-question'),
    path(r"^comments/", include("pinax.comments.urls", namespace="pinax_comments")),
    path(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    path(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    path('faq/',views.faq,name='faq_page'),

   url(r'^contact/$', views.contact, name='contact'),
   url(r'^contact/thanks/$', views.thanks, name='thanks'),
   url(r'^privacy_page/$',views.policies, name='privacy_page'),
   path('university/',views.University,name='university_page'),
   path('computer_science/',views.ComputerScience,name='computer_science'),
   path('cities/',views.TOPCities,name='cities'),
   path('lahore/',views.Lahore,name='lahore_city'),
   path('ratings/',views.Pixar_rating,name='pixar_rating'),
   path('whatisreview/',views.WhatisReview,name='whatisreview'),
   path('donation/',views.Donation,name='donationpage'),
   path('jazzcash/',views.JazzCash,name='jazzcashpage'),
   path('hacking/',views.Hacking_Page,name='Hacking_page'),
   path('utility/',views.Utility,name='utility'),
   path('course1/',views.Wireless_Hacking,name='Wireless_Hacking_Course'),
   path('payment/',views.Payment,name='payment'),





    ]

