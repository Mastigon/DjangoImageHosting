from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, CreateView, DeleteView

menu = [{'title': "Главная", 'url_name': 'home', 'url': '/'},
        {'title': "Добавить картинку", 'url_name': 'add', 'url': '/upload/'}
        ]


class PicturesHome(ListView):
    model = Pictures
    template_name = 'pictures/index.html'
    extra_context = {'title': 'Главная страница'}
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


class AddPicture(CreateView):
    form_class = AddPostForm
    template_name = 'pictures/upload.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить картинку'
        context['menu'] = menu
        return context


class DeletePicture(DeleteView):
    model = Pictures
    template_name = 'pictures/delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить картинку'
        context['menu'] = menu
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')