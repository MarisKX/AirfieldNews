# Generated by Django 4.0.2 on 2022-03-03 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.CharField(default='A', max_length=8)),
                ('heading', models.CharField(max_length=2048)),
                ('posted_by', models.CharField(default='AirfieldNews', max_length=64)),
                ('date', models.DateField()),
                ('source', models.CharField(max_length=64)),
                ('original_post', models.URLField(blank=True, max_length=2048, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagsAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('display_name', models.CharField(max_length=64)),
                ('tag_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_tags', to='article.article')),
                ('tag_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_tag_name', to='article.tagsall')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleElements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SH', 'SubHeading'), ('TX', 'TextField'), ('TW', 'TwitterEmbed'), ('IM', 'ImageField'), ('QT', 'Quote')], default='TX', max_length=2)),
                ('article_element_content_subheading', models.CharField(blank=True, max_length=2048, null=True)),
                ('article_element_content_text', models.TextField(blank=True, null=True)),
                ('article_element_content_twitter', models.CharField(blank=True, max_length=2048, null=True)),
                ('article_element_content_image', models.ImageField(blank=True, max_length=2048, null=True, upload_to='')),
                ('article_element_content_quote', models.CharField(blank=True, max_length=1024, null=True)),
                ('article_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_elements', to='article.article')),
            ],
        ),
    ]
