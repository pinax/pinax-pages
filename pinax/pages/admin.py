from django.contrib import admin

import reversion.admin as VersionAdmin

from .models import Page


class PageAdmin(VersionAdmin):
    pass


admin.site.register(Page, PageAdmin)
