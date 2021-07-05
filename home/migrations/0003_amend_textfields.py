# Generated by Django 3.2.5 on 2021-07-01 14:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_add_contactpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='body',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='regionpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True),
        ),
    ]