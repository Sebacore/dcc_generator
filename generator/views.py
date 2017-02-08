from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Character
from .forms import CharacterForm


class CharacterListView(ListView):
    model = Character


class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterForm


class CharacterDetailView(DetailView):
    model = Character


class CharacterUpdateView(UpdateView):
    model = Character
    form_class = CharacterForm


def index(request):
    return render(request, 'generator/index.html')
