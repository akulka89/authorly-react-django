from django.contrib import admin
from .models import Profile, Tag, Article, Comment, Like, Discussion, Message, Suggestion

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Discussion)
admin.site.register(Message)
admin.site.register(Suggestion)
