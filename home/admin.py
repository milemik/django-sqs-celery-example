from django.contrib import admin

from home.models import UserInput


@admin.register(UserInput)
class UserInputAdmin(admin.ModelAdmin):
    pass
