from __future__ import unicode_literals

from django.conf import settings  # noqa

from appconf import AppConf

from .utils import load_path_attr


class PinaxPagesAppConf(AppConf):

    HOOKSET = "pinax.pages.hooks.DefaultHookSet"
    PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/"
    MARKUP_RENDERER = "markdown.markdown"

    def configure_markup_renderer(self, value):
        return load_path_attr(value)

    def configure_hookset(self, value):
        return load_path_attr(value)()

    class Meta:
        prefix = "pinax_pages"
