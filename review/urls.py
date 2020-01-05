"""review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include
from users import views as user_views
from django.conf.urls import url
from machina import urls as machina_urls
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from elearning import urls
import djangocms_comments
from users.views import activate
from blogger import urls
from django.views.i18n import JavaScriptCatalog
from freecourses import urls
from calculator import urls
urlpatterns = [
    path('secret_admin_panel/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('education/',include('djangoproject.urls')),


    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm2.html'),name='password_reset_confirm'),
    path('password_reset_done/',auth_views.PasswordResetView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('forum/', include(machina_urls)),
    path(r"^ratings/", include("pinax.ratings.urls", namespace="pinax_ratings")),
    path(r'^captcha/', include('captcha.urls')),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        user_views.activate, name='activate'),
    path(r"^ratings/", include("pinax.ratings.urls",namespace="pinax_ratings")),
    path(r"^comments/", include("pinax.comments.urls", namespace="pinax_comments")),
    path(r'^froala_editor/', include('froala_editor.urls')),

    path('blogs/',include('blogger.urls')),

    path('freecourse/',include('freecourses.urls')),
    path('cal/', include('calculator.urls'),name='calculator_page'),
    path('elearning/',include('elearning.urls')),
path(r'comments/', include('django_comments_xtd.urls')),
    path('',include('homepage.urls')),
path('djrichtextfield/', include('djrichtextfield.urls')),
path(r'jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('comment/',include('reviews.urls')),

    path('coder/',include('coder.urls')),
path('martor/', include('martor.urls')),





    




] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)







