from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
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
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # EXAMPLE TWEETS
    # https://twitter.com/UniteWestMids/status/1408412825857445889
    # https://twitter.com/unitetheunion/status/1408408131894333442
    # https://twitter.com/unite_west/status/1408341874830622720

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('twitter_handle'),
        StreamFieldPanel('body')
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
    
    parent_page_types = ['home.Homepage']
    subpage_types = []
