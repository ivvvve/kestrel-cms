from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel, InlinePanel, TabbedInterface, ObjectList
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

class RegionPage(Page):

    # content panels
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    standfirst = RichTextField(blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('embed', EmbedBlock()),
        ('link', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('body', blocks.RichTextBlock()),
            ('link_text', blocks.CharBlock()),
            ('link', blocks.URLBlock()),
        ]))
    ],blank=True)
    # menu panels
    menu = StreamField([
        ('menu_item', blocks.StructBlock([
            ('link_text', blocks.CharBlock()),
            ('link', blocks.URLBlock()),
        ]))
    ],blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('standfirst', classname="full"),
        StreamFieldPanel('body'),
    ]
    menu_panels = [
        StreamFieldPanel('menu'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(menu_panels, heading='Site Menu'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])

class ContactPage(Page):

    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField(blank=True)

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
    name = models.CharField(max_length=255, verbose_name='Contact Group Name')
    
    panels = [
        FieldPanel('name'),
        InlinePanel('related_contact_details'),
    ]

class ContactDetails(Orderable):
    id = models.AutoField(primary_key=True)
    page = ParentalKey(ContactGroups, on_delete=models.CASCADE, related_name='related_contact_details')
    name = models.CharField(max_length=255, verbose_name='Full Name')
    job = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    
    panels = [
        FieldPanel('name'),
        FieldPanel('job'),
        FieldPanel('telephone'),
        FieldPanel('email'),
    ]