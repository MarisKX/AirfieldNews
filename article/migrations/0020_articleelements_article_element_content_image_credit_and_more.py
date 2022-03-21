# Generated by Django 4.0.2 on 2022-03-21 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_alter_article_article_insight'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleelements',
            name='article_element_content_image_credit',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='articleelements',
            name='article_element_content_image_desc',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_category', to='article.category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='article.regions'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_sub_category', to='article.subcategory'),
        ),
        migrations.AlterField(
            model_name='article',
            name='source',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='articleelements',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='element_type', to='article.elementtype'),
        ),
    ]
