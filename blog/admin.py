#coding=utf8
from django.contrib import admin
from blog.models import Article, Tag, Comment, BugTalk, BugTalkInline, About
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.models import MarkdownField

class ArticleAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(BugTalk)
admin.site.register(BugTalkInline)
admin.site.register(About)