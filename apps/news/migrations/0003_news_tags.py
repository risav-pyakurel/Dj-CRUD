# Generated by Django 5.1.1 on 2024-09-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_is_active'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(related_name='news', to='tags.tag'),
        ),
    ]
