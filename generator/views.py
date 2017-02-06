from django.shortcuts import get_object_or_404, render
from .models import Character


def index(request):
    character_list = Character.objects.order_by('name')
    context = {'character_list': character_list, }
    return render(request, 'generator/index.html', context)


def detail(request, character_name):
    character = get_object_or_404(Character, name=character_name)
    return render(request, 'generator/details.html', {'character': character})
