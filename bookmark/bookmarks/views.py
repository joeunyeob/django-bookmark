from django.shortcuts import render
from .models import Bookmark
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy
    template_name_suffix = '_create'


