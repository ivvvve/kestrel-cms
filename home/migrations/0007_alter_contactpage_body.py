# Generated by Django 3.2.5 on 2021-07-01 15:03

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210701_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
