from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import time


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your RYP Account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': User,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(User.pk)),
                'token': account_activation_token.make_token(User),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created . Check Your Email For Email Verification ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Activation link is invalid! Send Us Your Detail At rypnotifications@gmail.com')

    else:
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            request.session.set_expiry(86400)
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }




    return render(request, 'users/profile.html', context)





