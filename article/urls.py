from django.urls import path
from . import views

urlpatterns = [
    path('article/<article_number>/', views.article, name='article'),
]
