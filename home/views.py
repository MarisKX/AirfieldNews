from django.shortcuts import render, get_object_or_404, redirect, reverse
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
    regions = Regions.objects.all().order_by('display_name')

    query_filter_category = None
    query_filter_region = None
    query_filter_tag = None
    query_search_all = None

    latest_articles_by_category = []

    for category in categories:
        article_by_category = Article.objects.filter(article_category=category).order_by('-date')[:6]
        latest_articles_by_category.append(article_by_category)

    if latest_articles.count() >= 10:

        if request.GET:
            # Handles main filtering functionality
            if 'q' in request.GET:
                query_search_all = request.GET['q']
                if not query_search_all:
                    # messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('home'))
                
                queries = Q(
                    heading__icontains=query_search_all) | Q(
                    article_insight__icontains=query_search_all) | Q(
                    article_elements__article_element_content_text__icontains=query_search_all) | Q(
                    article_tags__tag_name__name__icontains=query_search_all)
                all_articles = all_articles.filter(queries).distinct()

                context = {
                        'query_search_all': query_search_all,
                        'all_articles': all_articles,
                        'categories': categories,
                        'regions': regions,
                        'tags': tags,
                    }
                return render(request, 'categories/search-results.html', context)

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

            if 'region' in request.GET:
                query_filter_region = request.GET['region']

                queries = Q(
                    article_region__name__icontains=query_filter_region)
                all_articles = all_articles.filter(queries)
                selected_region = get_object_or_404(Regions, name=query_filter_region)

                context = {
                    'query_filter_region': query_filter_region,
                    'all_articles': all_articles,
                    'selected_category': selected_region,
                    'categories': categories,
                    'regions': regions,
                    'tags': tags,
                }
                return render(request, 'categories/regions.html', context)

            if 'tag' in request.GET:
                query_filter_tag = request.GET['tag']

                queries = Q(
                    article_tags__tag_name__name__icontains=query_filter_tag)
                all_articles = all_articles.filter(queries).distinct()
                selected_tag = get_object_or_404(TagsAll, name=query_filter_tag)

                context = {
                    'query_filter_region': query_filter_region,
                    'all_articles': all_articles,
                    'selected_tag': selected_tag.tag_name,
                    'categories': categories,
                    'regions': regions,
                    'tags': tags,
                }
                return render(request, 'categories/tags.html', context)

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
