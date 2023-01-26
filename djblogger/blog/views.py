from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "blog/index.html"
