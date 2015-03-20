# coding:utf-8
from django.shortcuts import render
from depotwork.activities.models import Notification, AppNotification
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

from depotwork.decorators import ajax_required
from depotwork.settings import REDIRECT_FIELD_NAME, PAGINATOR_NUM


@login_required
def notifications(request):
    user = request.user
    notification_type = request.GET.get('notification_type')
    if notification_type == 'site':
        unread = Notification.objects.filter(to_user=user, is_read=False)
    else:
        notification_type = 'app'
        unread = AppNotification.objects.filter(to_user=user, is_read=False)
    paginator = Paginator(unread, PAGINATOR_NUM)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'activities/ace_notifications.html', {
        'notification_type': notification_type,
        'unread_num': len(unread),
        'unread': contacts,
    })


# @login_required
@ajax_required
def check_notifications(request):
    user = request.user
    if user.is_authenticated():
        notifications = Notification.objects.filter(to_user=user, is_read=False)
        appnotifications = AppNotification.objects.filter(to_user=user, is_read=False)
        count = len(notifications) + len(appnotifications)
        return HttpResponse(count)
    else:
        return HttpResponse(0)


# @login_required
@ajax_required
def last_notifications(request):
    # 后期在这里将站内通知 合并一起送出
    if request.user.is_authenticated():
        status = 'succeed'
        user = request.user
        site_notifications = Notification.objects.filter(to_user=user, is_read=False)
        site_count = len((site_notifications))
        app_notifications = AppNotification.objects.filter(to_user=user, is_read=False)
        app_count = len(app_notifications)
        # 读取全部的App通知，当大于6条时，站点通知就不读取
        if app_count > 6:
            s_point = 0
            app_count = 6
        else:
            s_point = 6 - app_count
        count = app_count + site_count
        data = render(request, 'activities/last_notifications.html', {
            'site_notifications': site_notifications[:s_point],
            'app_notifications': app_notifications,
            'unread_notification_num': count
        })
    else:
        status = 'un_auth'
        data = render(request, 'core/need_login.html', {'current_url': request.REQUEST.get('current')})
    return HttpResponse(json.dumps({'status': status, 'data': data.content}), content_type='application/json')


@login_required
def make_notification_read(request):
    user = request.user
    type = request.GET.get('notification_type')
    id = request.GET.get('notification_id')
    next = request.GET.get('next')
    if type == 'app':
        n = AppNotification.objects.get(id=id)
    elif type == 'site':
        n = Notification.objects.get(id=id)
    n.is_read = True
    n.save()
    return HttpResponseRedirect(next)