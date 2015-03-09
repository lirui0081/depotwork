# coding:utf-8

from django.shortcuts import render
from django.utils.translation import ugettext

# Create your views here.


def all_notification(req):
    pass


def home(req):
    user = {}
    user['name'] = ugettext('feed')
    return render(req, 'asset/index.html', {'user': user})