# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape


class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    feed = models.IntegerField(null=True, blank=True)
    question = models.IntegerField(null=True, blank=True)
    answer = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __unicode__(self):
        return self.activity_type


# def save(self, *args, **kwargs):
# super(Activity, self).save(*args, **kwargs)
# if self.activity_type == Activity.FAVORITE:
# Question = models.get_model('questions', 'Question')
# question = Question.objects.get(pk=self.question)
# user = question.user
# user.profile.reputation = user.profile.reputation + 5
# user.save()

class Notification(models.Model):
    LIKED = 'L'
    COMMENTED = 'C'
    FAVORITED = 'F'
    ANSWERED = 'A'
    ACCEPTED_ANSWER = 'W'
    EDITED_ARTICLE = 'E'
    ALSO_COMMENTED = 'S'
    NOTIFICATION_TYPES = (
        (LIKED, 'Liked'),
        (COMMENTED, 'Commented'),
        (FAVORITED, 'Favorited'),
        (ANSWERED, 'Answered'),
        (ACCEPTED_ANSWER, 'Accepted Answer'),
        (EDITED_ARTICLE, 'Edited Article'),
        (ALSO_COMMENTED, 'Also Commented'),
    )

    # _LIKED_TEMPLATE = u'<a href="/{0}/"><div class="user"><img src="{1}" class="user-picture">{2}</a> 赞了你的帖:</div>' \
    #                   u'<span class="label label-info"><a style="border-top: 0px" href="/feeds/{3}/">' \
    #                   u'<i class="menu-icon fa fa-list-alt"></i>{4}</a></span>'
    _LIKED_TEMPLATE=  u'<a href="/notification/read?notification_type=site&notification_id={0}&next=/feeds/{1}/">' \
                      u'<div class="clearfix"> ' \
                      u'<span class="pull-left "><div class="user"><img src="{2}" class="user-picture"></div>{3}</span>' \
                      u'<div class="clearfix"><span class="pull-right">赞了: {4}</span></div>' \
                      u'</div> '
    # _COMMENTED_TEMPLATE = u'<a href="/{0}/">{1}</a> 评论了你的帖: ' \
    #                       u'<a style="border-top: 0px" href="/feeds/{2}/">{3}</a>'
    _COMMENTED_TEMPLATE=  u'<a href="/notification/read?notification_type=site&notification_id={0}&next=/feeds/{1}/">' \
                      u'<div class="clearfix"> ' \
                      u'<span class="pull-left "><div class="user"><img src="{2}" class="user-picture"></div>{3}</span>' \
                      u'<div class="clearfix"><span class="pull-right">评论了: {4}</span></div>' \
                      u'</div> '
    # _FAVORITED_TEMPLATE = u'<a href="/{0}/">{1}</a>关注了你的问题: ' \
    #                       u'<a style="border-top: 0px" href="/questions/{2}/">{3}</a>'
    _FAVORITED_TEMPLATE=  u'<a href="/notification/read?notification_type=site&notification_id={0}&next=/questions/{1}/">' \
                      u'<div class="clearfix"> ' \
                      u'<span class="pull-left "><div class="user"><img src="{2}" class="user-picture"></div>{3}</span>' \
                      u'<div class="clearfix"><span class="pull-right">关注: {4}</span></div>' \
                      u'</div> '
    # _ANSWERED_TEMPLATE = u'<a href="/{0}/">{1}</a> 回答了你的问题: ' \
    #                      u'<a style="border-top: 0px" href="/questions/{2}/">{3}</a>'
    _ANSWERED_TEMPLATE=  u'<a href="/notification/read?notification_type=site&notification_id={0}&next=/questions/{1}/">' \
                      u'<div class="clearfix"> ' \
                      u'<span class="pull-left "><div class="user"><img src="{2}" class="user-picture"></div>{3}</span>' \
                      u'<div class="clearfix"><span class="pull-right">回答: {4}</span></div>' \
                      u'</div> '
    # _ACCEPTED_ANSWER_TEMPLATE = u'<a href="/{0}/">{1}</a> 接受了你的答案: ' \
    #                             u'<a style="border-top: 0px" href="/questions/{2}/">{3}</a>'
    _ACCEPTED_ANSWER_TEMPLATE=  u'<a href="/notification/read?notification_type=site&notification_id={0}&next=/questions/{1}/">' \
                      u'<div class="clearfix"> ' \
                      u'<span class="pull-left "><div class="user"><img src="{2}" class="user-picture"></div>{3}</span>' \
                      u'<div class="clearfix"><span class="pull-right">接受答案: {4}</span></div>' \
                      u'</div> '
    # _EDITED_ARTICLE_TEMPLATE = u'<a href="/{0}/">{1}</a> 编辑了你的文章: ' \
    #                            u'<a style="border-top: 0px" href="/article/{2}/">{3}</a>'
    _EDITED_ARTICLE_TEMPLATE=  u'<a href="/notification/read?notification_type=site&notification_id={0}&next=/article/{1}/">' \
                      u'<div class="clearfix"> ' \
                      u'<span class="pull-left "><div class="user"><img src="{2}" class="user-picture"></div>{3}</span>' \
                      u'<div class="clearfix"><span class="pull-right">编辑: {4}</span></div>' \
                      u'</div> '
    # _ALSO_COMMENTED_TEMPLATE = u'<a href="/{0}/">{1}</a> 也评论了贴: ' \
    #                            u'<a style="border-top: 0px" href="/feeds/{2}/">{3}</a>'
    _ALSO_COMMENTED_TEMPLATE=  u'<a href="/notification/read?notification_type=site&notification_id={0}&next=/feeds/{1}/">' \
                      u'<div class="clearfix"> ' \
                      u'<span class="pull-left "><div class="user"><img src="{2}" class="user-picture"></div>{3}</span>' \
                      u'<div class="clearfix"><span class="pull-right">也评论: {4}</span></div>' \
                      u'</div> '

    from_user = models.ForeignKey(User, related_name='+')
    to_user = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField(auto_now_add=True)
    feed = models.ForeignKey('feeds.Feed', null=True, blank=True)
    question = models.ForeignKey('questions.Question', null=True, blank=True)
    answer = models.ForeignKey('questions.Answer', null=True, blank=True)
    article = models.ForeignKey('articles.Article', null=True, blank=True)
    notification_type = models.CharField(max_length=1, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __unicode__(self):
        if self.notification_type == self.LIKED:
            return self._LIKED_TEMPLATE.format(
                self.pk,
                self.feed.pk,
                escape(self.from_user.profile.get_picture()),
                # escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                escape(self.get_summary(self.feed.post)),
            )
        elif self.notification_type == self.COMMENTED:
            return self._COMMENTED_TEMPLATE.format(
                self.pk,
                self.feed.pk,
                escape(self.from_user.profile.get_picture()),
                # escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                escape(self.get_summary(self.feed.post))
            )
        elif self.notification_type == self.FAVORITED:
            return self._FAVORITED_TEMPLATE.format(
                self.pk,
                self.question.pk,
                # escape(self.from_user.username),
                escape(self.from_user.profile.get_picture()),
                escape(self.from_user.profile.get_screen_name()),
                escape(self.get_summary(self.question.title))
            )
        elif self.notification_type == self.ANSWERED:
            return self._ANSWERED_TEMPLATE.format(
                self.pk,
                self.question.pk,
                # escape(self.from_user.username),
                escape(self.from_user.profile.get_picture()),
                escape(self.from_user.profile.get_screen_name()),
                escape(self.get_summary(self.question.title))
            )
        elif self.notification_type == self.ACCEPTED_ANSWER:
            return self._ACCEPTED_ANSWER_TEMPLATE.format(
                self.pk,
                self.answer.question.pk,
                # escape(self.from_user.username),
                escape(self.from_user.profile.get_picture()),
                escape(self.from_user.profile.get_screen_name()),
                escape(self.get_summary(self.answer.description))
            )
        elif self.notification_type == self.EDITED_ARTICLE:
            return self._EDITED_ARTICLE_TEMPLATE.format(
                self.pk,
                self.article.slug,
                # escape(self.from_user.username),
                escape(self.from_user.profile.get_picture()),
                escape(self.from_user.profile.get_screen_name()),
                escape(self.get_summary(self.article.title))
            )
        elif self.notification_type == self.ALSO_COMMENTED:
            return self._ALSO_COMMENTED_TEMPLATE.format(
                self.pk,
                # escape(self.from_user.username),
                escape(self.from_user.profile.get_picture()),
                escape(self.from_user.profile.get_screen_name()),
                escape(self.get_summary(self.feed.post))
            )
        else:
            return 'Ooops! Something went wrong.'

    def get_summary(self, value):
        summary_size = 7
        if len(value) > summary_size:
            return u'{0}...'.format(value[:summary_size])
        else:
            return value


# APP的 Activity 用于搜集汇总用户的参与行为
# 如参与菜品点赞
class AppActivity(models.Model):
    ASSET = 'A'
    ACTIVITY_TYPES = (
        (ASSET, u'资产管理'),
    )

    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'AppActivity'
        verbose_name_plural = 'AppActivities'

    def __unicode__(self):
        return self.activity_type


# APP Notification 泛化消息通知，应对可添加App模块，而不用改动表结构
class AppNotification(models.Model):
    # 列出使用的App

    # asset
    ASSET = 'AM'

    APPS_ICO = {
        ASSET: 'fa-eye'
    }
    APPS_NAME_DICT = {
        ASSET: u'资产管理'
    }

    RETURN_IN_NAVBAR_TEMPLATE = {
        ASSET: u'<a href="/notification/read?notification_type=app&notification_id={0}&next={1}">'
               u'<div class="clearfix"><span class="pull-left">'
               u'<i class="btn btn-xs no-hover btn-pink fa {2}"></i>  <b>{3}</b>  </span>'
               u'<span class="pull-right">  {4} </span></div> ',
    }
    RETURN_IN_ALL_TEMPLATE = {
        ASSET: u'',
    }

    APPS_NAME_TUPLE = tuple(APPS_NAME_DICT.items())

    from_user = models.ForeignKey(User, related_name='+')
    to_user = models.ForeignKey(User, related_name='+')
    from_app = models.CharField(max_length=3, choices=APPS_NAME_TUPLE)
    content = models.CharField(max_length=32)
    to_do_reference_url = models.CharField(max_length=2048)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AppNotification'
        verbose_name_plural = 'AppNotification'
        ordering = ('-date',)

    def __unicode__(self):
        for app in self.APPS_NAME_TUPLE:
            app_name_flag = app[0]
            if self.from_app == app_name_flag:
                return self.RETURN_IN_NAVBAR_TEMPLATE[app_name_flag].format(
                    self.pk,
                    escape(self.to_do_reference_url),
                    escape(self.APPS_ICO[app_name_flag]),
                    escape(self.APPS_NAME_DICT[app_name_flag]),
                    escape(self.content)
                )
        return 'Ooops! Something went wrong.'

    def get_ico(self):
        return self.APPS_ICO[self.from_app]

    def get_app_name(self):
        return self.APPS_NAME_DICT[self.from_app]