# Generated by Django 5.0.4 on 2024-05-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cms_slider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS Class'),
        ),
    ]