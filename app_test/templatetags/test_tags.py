# from django import template
# from django.db import models
#
# from Websiite.app_test.models import Directions
#
# register = template.Library()
#
#
# @register.simple_tag()
# def show_navigators():
#     navigators = [
#         {'title': 'О НАС', 'url_name': 'about','index': 1},
#         {'title': 'ВЫСТУПЛЕНИЯ', 'url_name': 'presentation','index': 2},
#         {'title': 'НОВОСТИ', 'url_name': 'news','index': 3},
#         {"title": "ОБРАТНАЯ СВЯЗЬ", "url_name": 'form', 'index': 4}
#     ]
#     return navigators
#
#
# @register.simple_tag()
# def show_directions():
#     directions = Directions.objects.all()
#     return directions
