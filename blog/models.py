#coding=utf-8
from django.db import models
from django_markdown.models import MarkdownField
from django_markdown.widgets import MarkdownWidget

class Tag(models.Model):
    tag = models.CharField(max_length=200)

    def __unicode__(self):
        return self.tag

class ArticleQueryset(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = ArticleQueryset.as_manager()
    tag = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ['-created']

class Comment(models.Model):
    article = models.ForeignKey(Article)
    name = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

class Comment_inline(models.Model):
    comment_pre = models.ForeignKey(Comment)
    name = models.CharField(max_length=200)
    pre_name = models.CharField(max_length=200)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name + self.pre_name

    class Meta:
        verbose_name = "多级评论"
        verbose_name_plural = "多级评论"

class BugTalk(models.Model):
    nick_name = models.CharField(max_length=200)
    pub_data = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return self.nick_name
    class Meta:
        verbose_name = "吐槽bug"
        verbose_name_plural = "吐槽bug"


class BugTalkInline(models.Model):
    bug_pre = models.ForeignKey(BugTalk)
    nick_name = models.CharField(max_length=200)
    name_pre = models.CharField(max_length=200)
    content = models.TextField()
    pub_data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nick_name

    class Meta:
        verbose_name = "吐槽bug回复"
        verbose_name_plural = "吐槽bug回复"
        ordering = ["-pub_data"]