from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from article.models import (
    Article,
    ArticleElements,
    Category,
    Regions,
    TagsAll,
)

# Create your views here.


def index(request):
    """ A view to return the index page """
    all_articles = Article.objects.all().order_by('-date')
    latest_articles = Article.objects.all().order_by('-date')[:4]
    categories = Category.objects.all()
    regions = Regions.objects.all()

    latest_articles_by_category = []

    for category in categories:
        article_by_category = Article.objects.filter(article_category=category).order_by('-date')[:3]
        latest_articles_by_category.append(article_by_category)

    print(latest_articles_by_category)
    if latest_articles:

        context = {
            'latest_articles': latest_articles,
            'categories': categories,
            'all_articles': all_articles,
            'latest_articles_by_category': latest_articles_by_category,
            'regions': regions,
        }

        return render(request, 'home/index.html', context)
    else:
        return render(request, 'temp/coming_soon.html')
