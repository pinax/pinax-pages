from django.conf.urls import url, patterns

from .views import file_index, file_create, file_download, file_delete, page_edit, page


PAGE_RE = r"(([\w-]{1,})(/[\w-]{1,})*)/"

urlpatterns = patterns(
    "",
    url(r"^files/$", file_index, name="file_index"),
    url(r"^files/create/$", file_create, name="file_create"),
    url(r"^files/(\d+)/([^/]+)$", file_download, name="file_download"),
    url(r"^files/(\d+)/delete/$", file_delete, name="file_delete"),
    url(r"^(?P<path>%s)_edit/$" % PAGE_RE, page_edit, name="cms_page_edit"),
    url(r"^(?P<path>%s)$" % PAGE_RE, page, name="cms_page"),
)
