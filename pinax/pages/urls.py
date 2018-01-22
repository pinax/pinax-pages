from django.conf.urls import url

from .conf import settings
from .views import file_index, file_create, file_download, file_delete, page_edit, page

app_name = "pinax_pages"

urlpatterns = [
    url(r"^files/$", file_index, name="file_index"),
    url(r"^files/create/$", file_create, name="file_create"),
    url(r"^files/(\d+)/([^/]+)$", file_download, name="file_download"),
    url(r"^files/(\d+)/delete/$", file_delete, name="file_delete"),
    url(r"^(?P<path>%s)_edit/$" % settings.PINAX_PAGES_PAGE_REGEX, page_edit, name="pages_page_edit"),
    url(r"^(?P<path>%s)$" % settings.PINAX_PAGES_PAGE_REGEX, page, name="pages_page"),
]
