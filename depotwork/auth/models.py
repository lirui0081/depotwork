# coding:utf-8
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings
import os.path
from depotwork.activities.models import Notification
import urllib, hashlib
no_picture = settings.STATIC_URL + '/base_from_ace/avatars/user.jpg'

class Profile(models.Model):
    user = models.OneToOneField(User)
    # full_name = models.CharField(max_length=20,null=True, blank=True,verbose_name=u'姓名')
    # motto = models.CharField(max_length=20,null=True, blank=True,verbose_name=u'座右铭')
    job_title = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True,verbose_name=u'住址')
    # phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=u'联系电话')
    # date = models.DateField(auto_now_add=True,verbose_name=u'更新时间')


    def get_picture(self):
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' + self.user.username + '.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' + self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                gravatar_url = no_picture
                return gravatar_url
        except Exception, e:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username

    def notify_liked(self, feed):
        if self.user != feed.user:
            Notification(notification_type=Notification.LIKED,
                         from_user=self.user,
                         to_user=feed.user,
                         feed=feed).save()

    def unotify_liked(self, feed):
        if self.user != feed.user:
            Notification.objects.filter(notification_type=Notification.LIKED,
                                        from_user=self.user,
                                        to_user=feed.user,
                                        feed=feed).delete()

    def notify_commented(self, feed):
        if self.user != feed.user:
            Notification(notification_type=Notification.COMMENTED,
                         from_user=self.user,
                         to_user=feed.user,
                         feed=feed).save()

    def notify_also_commented(self, feed):
        comments = feed.get_comments()
        users = []
        for comment in comments:
            if comment.user != self.user and comment.user != feed.user:
                users.append(comment.user.pk)
        users = list(set(users))
        for user in users:
            Notification(notification_type=Notification.ALSO_COMMENTED,
                         from_user=self.user,
                         to_user=User(id=user),
                         feed=feed).save()

    def notify_favorited(self, question):
        if self.user != question.user:
            Notification(notification_type=Notification.FAVORITED,
                         from_user=self.user,
                         to_user=question.user,
                         question=question).save()

    def unotify_favorited(self, question):
        if self.user != question.user:
            Notification.objects.filter(notification_type=Notification.FAVORITED,
                                        from_user=self.user,
                                        to_user=question.user,
                                        question=question).delete()

    def notify_answered(self, question):
        if self.user != question.user:
            Notification(notification_type=Notification.ANSWERED,
                         from_user=self.user,
                         to_user=question.user,
                         question=question).save()

    def notify_accepted(self, answer):
        if self.user != answer.user:
            Notification(notification_type=Notification.ACCEPTED_ANSWER,
                         from_user=self.user,
                         to_user=answer.user,
                         answer=answer).save()

    def unotify_accepted(self, answer):
        if self.user != answer.user:
            Notification.objects.filter(notification_type=Notification.ACCEPTED_ANSWER,
                                        from_user=self.user,
                                        to_user=answer.user,
                                        answer=answer).delete()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)