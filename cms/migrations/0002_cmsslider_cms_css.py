# Generated by Django 3.1.7 on 2021-03-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='active', max_length=100, verbose_name='CSS class'),
            preserve_default=False,
        ),
    ]
