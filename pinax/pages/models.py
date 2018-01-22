import os

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .hooks import hookset
from .managers import PublishedPageManager


class Page(models.Model):

    STATUS_CHOICES = (
        (1, _("Draft")),
        (2, _("Public")),
    )

    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    body_html = models.TextField(blank=True, editable=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    publish_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated = models.DateTimeField(editable=False, default=timezone.now)

    published = PublishedPageManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pinax_pages:pages_page", args=[self.path])

    @property
    def is_community(self):
        return self.path.lower().startswith("community/")

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        self.body_html = hookset.parse_content(self.body)
        super(Page, self).save(*args, **kwargs)
        self.pagehistory_set.create(
            title=self.title,
            path=self.path,
            body=self.body,
            body_html=self.body_html,
            status=self.status,
            publish_date=self.publish_date
        )

    def clean_fields(self, exclude=None):
        super(Page, self).clean_fields(exclude)
        hookset.validate_path(self.path)


class PageHistory(models.Model):

    page = models.ForeignKey(Page, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100, editable=False)
    path = models.CharField(max_length=100, editable=False)
    body = models.TextField(editable=False)
    body_html = models.TextField(blank=True, editable=False)
    status = models.IntegerField(default=2, editable=False)
    publish_date = models.DateTimeField(default=timezone.now, editable=False)
    created = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return "{} - {}".format(self.title, self.created)


def generate_filename(instance, filename):
    return filename


class File(models.Model):

    file = models.FileField(upload_to=generate_filename)
    created = models.DateTimeField(default=timezone.now)

    def download_url(self):
        return reverse("pinax_pages:file_download", args=[self.pk, os.path.basename(self.file.name).lower()])
