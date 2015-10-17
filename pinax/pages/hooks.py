import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class DefaultHookSet(object):

    def __init__(self):
        from .conf import settings  # if put globally there is a race condition
        self.settings = settings

    def parse_content(self, content):
        return self.settings.PINAX_PAGES_MARKUP_RENDERER(content)

    def validate_path(self, path):
        if not re.match(self.settings.PINAX_PAGES_PAGE_REGEX, path):
            raise ValidationError({
                "path": [
                    _("Path can only contain letters, numbers and hyphens and end with /")
                ]
            })


class HookProxy(object):

    def __getattr__(self, attr):
        from .conf import settings  # if put globally there is a race condition
        return getattr(settings.PINAX_PAGES_HOOKSET, attr)


hookset = HookProxy()
