from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article, ArticleElements, Category, TagsAll, ArticleTags


def article(request, article_number):
    """ A view to show individual product details """

    categories = Category.objects.all()
    article = get_object_or_404(Article, article_number=article_number)
    article_elements = ArticleElements.objects.filter(article_number=article).order_by('sequence')
    article_tags = ArticleTags.objects.filter(article_number=article).order_by('tag_name')
    tags = TagsAll.objects.all().order_by('display_name')

    context = {
        'article': article,
        'article_elements': article_elements,
        'categories': categories,
        'article_tags': article_tags,
        'tags': tags
    }

    return render(request, 'article/article.html', context)
