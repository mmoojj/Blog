# Generated by Django 4.2.6 on 2023-10-15 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس')),
                ('description', models.TextField(verbose_name='محتوا')),
                ('sumbnail', models.ImageField(upload_to='images', verbose_name='تصویر')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]