from django.contrib import admin

from .models import Post, Contributor, SocialMediaIcon, QLA, WeeklyVignette

admin.site.register(Post)
admin.site.register(Contributor)
admin.site.register(SocialMediaIcon)
admin.site.register(QLA)
admin.site.register(WeeklyVignette)
