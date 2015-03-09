# coding:utf-8
from django.shortcuts import render
from depotwork.activities.models import Notification, AppNotification
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from depotwork.decorators import ajax_required


@login_required
def notifications(request):
    user = request.user
    notification_type = request.GET.get('notification_type')
    if notification_type == 'site':
        unread = Notification.objects.filter(to_user=user, is_read=False)
    else:
        notification_type = 'app'
        unread = AppNotification.objects.filter(to_user=user, is_read=False)
    paginator = Paginator(unread, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    print notification_type
    return render(request, 'activities/ace_notifications.html', {
        'notification_type': notification_type,
        'unread_num': len(unread),
        'unread': contacts,
    })


@login_required
@ajax_required
def check_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user, is_read=False)[:4]
    appnotifications = AppNotification.objects.filter(to_user=user, is_read=False)[:4]
    count = len(notifications) + len(appnotifications)
    return HttpResponse(count)


@login_required
@ajax_required
def last_notifications(request):
    # 后期在这里将站内通知 合并一起送出
    user = request.user
    site_notifications = Notification.objects.filter(to_user=user, is_read=False)
    site_count = len((site_notifications))
    app_notifications = AppNotification.objects.filter(to_user=user, is_read=False)
    app_count = len(app_notifications)
    # 读取全部的App通知，当大于10条时，站点通知就不读取
    if app_count > 10:
        s_point = 0
    else:
        s_point = 10 - app_count
    count = app_count + site_count
    return render(request, 'activities/last_notifications.html', {
        'site_notifications': site_notifications,
        'app_notifications': app_notifications[:s_point],
        'unread_notification_num': count
    })


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