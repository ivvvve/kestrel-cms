from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel


class HomePage(Page):
    pass

class RegionPage(Page):

    twitter_handle = models.CharField(max_length=200)
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('twitter_handle'),
        FieldPanel('body', classname="full"),

    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
    
    parent_page_types = ['home.Homepage']
    subpage_types = []
