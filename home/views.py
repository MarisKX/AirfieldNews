from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    """ A view to return the index page """

    context = {
    }

    return render(request, 'home/index.html', context)
