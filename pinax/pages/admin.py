from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import Page


class PageAdmin(VersionAdmin):
    pass


admin.site.register(Page, PageAdmin)
