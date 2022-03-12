from datetime import *
from django.utils import timezone
from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)
    submenu = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class SubCategory(models.Model):
    main_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='main_category')
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class ElementType(models.Model):
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)
    jinja_name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the article number
        if it hasn't been set already.
        """
        self.jinja_name = f"includes/article_elements/{self.name}.html"
        super().save(*args, **kwargs)


class TagsAll(models.Model):
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)
    tag_name = models.CharField(max_length=64, default="a")

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the article number
        if it hasn't been set already.
        """
        self.tag_name = f"#{self.display_name}"
        super().save(*args, **kwargs)


class Regions(models.Model):
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Article(models.Model):
    article_number = models.CharField(max_length=8, default="1")
    article_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='article_category')
    article_sub_category = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name='article_sub_category')
    article_region = models.ForeignKey(Regions, null=True, blank=True, on_delete=models.SET_NULL, related_name='region')
    article_image = models.ImageField(null=True, blank=True)
    heading = models.CharField(max_length=2048)
    article_insight = models.CharField(max_length=300)
    posted_by = models.CharField(max_length=64, default="AirfieldNews")
    date = models.DateField(auto_now_add=False)
    source = models.CharField(max_length=64)
    original_post = models.URLField(max_length=2048, null=True, blank=True)

    def _generate_article_number(self):
        """
        Generate a random, unique article number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the article number
        if it hasn't been set already.
        """
        if self.article_number == "1":
            self.article_number = self._generate_article_number()
        super().save(*args, **kwargs)


class ArticleElements(models.Model):
    article_number = models.ForeignKey(Article, null=False, blank=False, on_delete=models.CASCADE, related_name='article_elements')
    sequence = models.IntegerField(default=1)
    type = models.ForeignKey(ElementType, null=True, blank=True, on_delete=models.CASCADE, related_name='element_type')

    article_element_content_subheading = models.CharField(max_length=2048, null=True, blank=True)
    article_element_content_text = models.TextField(null=True, blank=True)
    article_element_content_twitter = models.CharField(max_length=2048, null=True, blank=True)
    article_element_content_image = models.ImageField(max_length=2048, null=True, blank=True)
    article_element_content_quote = models.CharField(max_length=1024, null=True, blank=True)


class ArticleTags(models.Model):
    article_number = models.ForeignKey(Article, null=False, blank=False, on_delete=models.CASCADE, related_name='article_tags')
    tag_name = models.ForeignKey(TagsAll, null=False, blank=False, on_delete=models.CASCADE, related_name='article_tag_name')

