# Generated by Django 4.2.6 on 2023-10-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_article_category_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='articles', to='blog.category', verbose_name='دسته بندی'),
        ),
    ]
