from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.pages"
    label = "pinax_pages"
    verbose_name = _("Pinax Pages")
