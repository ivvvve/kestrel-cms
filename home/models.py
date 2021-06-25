from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class HomePage(Page):
    pass

class RegionPage(Page):

    twitter_handle = models.CharField(max_length=200)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock())
    ])

    content_panels = Page.content_panels + [
        FieldPanel('twitter_handle'),
        StreamFieldPanel('body')
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
    
    parent_page_types = ['home.Homepage']
    subpage_types = []
