from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy

from .models import Article



class ArticleListView(LoginRequiredMixin, ListView):
    model =Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model =Article
    template_name = 'articles_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model =Article
    fields = ('title', 'body',)
    template_name = 'articles_edit.html'
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model =Article
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model =Article
    template_name = 'articles_new.html'
    fields = ('title', 'body', )
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)




# Create your views here.
