from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class MemberAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("__str__")

admin.site.register(User)
admin.site.register(Member)
admin.site.register(Article)