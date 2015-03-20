# coding:utf-8

from django.shortcuts import render
from django.utils.translation import ugettext
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_notification(req):
    pass

@login_required
def home(req):

    return render(req, 'asset/index.html')