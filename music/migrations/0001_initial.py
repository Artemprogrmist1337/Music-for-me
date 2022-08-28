# Generated by Django 4.1 on 2022-08-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mus_file', models.FileField(upload_to='music_files/%Y/%m/%d/')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('text', models.TextField(blank=True, verbose_name='Текст песни')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Музыка',
                'verbose_name_plural': 'Музыки',
                'ordering': ['-created_at'],
            },
        ),
    ]