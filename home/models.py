from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

class RegionPage(Page):

    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('embed', EmbedBlock())
    ],
    blank=True
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        StreamFieldPanel('body')
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]

class ContactPage(Page):

    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField()

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('body', classname="full"),
        InlinePanel('related_contact_groups', label="Related contact groups"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
    
class ContactGroups(ClusterableModel):
    id = models.AutoField(primary_key=True)
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='related_contact_groups')
    name = models.CharField(max_length=255)
    
    panels = [
        FieldPanel('name'),
        InlinePanel('related_contact_details'),
    ]


class ContactDetails(Orderable):
    id = models.AutoField(primary_key=True)
    page = ParentalKey(ContactGroups, on_delete=models.CASCADE, related_name='related_contact_details')
    name = models.CharField(max_length=255)
    
    panels = [
        FieldPanel('name')
    ]