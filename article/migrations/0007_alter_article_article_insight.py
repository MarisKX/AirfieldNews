# Generated by Django 4.0.2 on 2022-03-04 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_article_insight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_insight',
            field=models.CharField(max_length=128),
        ),
    ]
