# Generated by Django 4.1 on 2022-08-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='music',
            name='like',
            field=models.BooleanField(blank=True, default=True, verbose_name='Нравится'),
        ),
    ]
