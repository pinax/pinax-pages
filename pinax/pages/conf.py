from __future__ import unicode_literals

from django.conf import settings  # noqa

from appconf import AppConf


class PinaxPagesAppConf(AppConf):

    PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/"

    class Meta:
        prefix = "pinax_pages"
