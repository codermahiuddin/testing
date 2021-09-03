# Generated by Django 3.2.6 on 2021-09-01 09:56

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tages',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
