# coding:utf-8
import os
import json
from PIL import Image

from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.conf import settings as django_settings
from django.utils.http import is_safe_url
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from depotwork.decorators import ajax_required
from depotwork.core.forms import ProfileForm, ChangePasswordForm
from depotwork.feeds.views import feeds
from depotwork.feeds.models import Feed
from depotwork.feeds.views import FEEDS_NUM_PAGES
from depotwork.settings import REDIRECT_FIELD_NAME


def home(request):
    if request.user.is_authenticated():
        return feeds(request)
    else:
        return render(request, 'core/cover.html', {'next': request.REQUEST.get('next')})


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.user.is_authenticated():
        redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(django_settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


@login_required
def settings(request):
    return render(request, 'core/settings.html', )


@login_required
@ajax_required
def update_avatar(request):
    response_data = []
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps(response_data.append({'status': 'fail'})), content_type='application/json')
    profile_pictures = django_settings.MEDIA_ROOT + '/profile_pictures/'
    avatar_image_width = django_settings.AVATAR_IMAGE_WIDTH
    if not os.path.exists(profile_pictures):
        os.makedirs(profile_pictures)
    f = request.FILES['avatar']
    filename = profile_pictures + request.user.username + '.jpg'
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    im = Image.open(filename)
    width, height = im.size
    if width > avatar_image_width:
        new_width = avatar_image_width
        new_height = (height * avatar_image_width) / width
        new_size = new_width, new_height
        im.thumbnail(new_size, Image.ANTIALIAS)
        im.save(filename)
    update_info = {}
    update_info['status'] = "OK"
    update_info['url'] = django_settings.MEDIA_URL + '/profile_pictures/' + request.user.username + '.jpg'
    update_info['message'] = u'上传成功'
    response_data.append(update_info)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required
@ajax_required
def update_profile(request):
    response_data = {}
    # 读取数据写入数据库
    return HttpResponse(json.dumps(response_data), content_type='application/json')


@login_required
def password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your password were successfully changed.')
    else:
        form = ChangePasswordForm(instance=user)
    return render(request, 'core/password.html', {'form': form})
