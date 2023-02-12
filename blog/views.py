from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePageView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title','body','author']

class EditPostView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


