from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
    latest_articles = Article.objects.all().order_by('-date')[:6]
    categories = Category.objects.all()
    tags = TagsAll.objects.all().order_by('display_name')
    regions = Regions.objects.all()

    query_filter_category = None

    latest_articles_by_category = []

    for category in categories:
        article_by_category = Article.objects.filter(article_category=category).order_by('-date')[:4]
        latest_articles_by_category.append(article_by_category)

    if latest_articles.count() >= 4:

        if request.GET:
            # Handles main filtering functionality
            if 'category' in request.GET:
                query_filter_category = request.GET['category']

                queries = Q(
                    article_category__name__icontains=query_filter_category)
                all_articles = all_articles.filter(queries)
                selected_category = get_object_or_404(Category, name=query_filter_category)

                context = {
                    'query_filter_category': query_filter_category,
                    'all_articles': all_articles,
                    'selected_category': selected_category,
                    'categories': categories,
                    'regions': regions,
                    'tags': tags,
                }
                return render(request, 'categories/categories.html', context)

        context = {
            'latest_articles': latest_articles,
            'categories': categories,
            'all_articles': all_articles,
            'latest_articles_by_category': latest_articles_by_category,
            'regions': regions,
            'tags': tags,
            'query_filter_category': query_filter_category
        }

        return render(request, 'home/index.html', context)
    else:
        return render(request, 'temp/coming_soon.html')
