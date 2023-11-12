from django.shortcuts import get_object_or_404

# from .models import *
from .forms import *
import re


main_menu = [
    {'title': 'О НАС', 'url_name': 'about', 'index': 1},
    {'title': 'ВЫСТУПЛЕНИЯ', 'url_name': 'presentation', 'index': 2},
    {'title': 'НОВОСТИ', 'url_name': 'news', 'index': 3},
    {"title": "ОБРАТНАЯ СВЯЗЬ", "url_name": 'form', 'index': 4},
    {"title": "ТЕСТ СВЯЗЬ", "url_name": 'test', 'index': 5}
]

contacts = [
    {"massage_name": "VK1","url_page": 'vk'},
    {"massage_name": "WA","url_page": 'wa'},
    {"massage_name": "TG","url_page": 'tg'}
]


class DataMixin:

    def get_user_context(self, **kwargs):
        directions = Directions.objects.all()
        form_test = FormTestFeed
        context = kwargs
        context["main_menu"] = main_menu
        context["directions"] = directions
        context["test"] = form_test
        print(form_test)
        return context




