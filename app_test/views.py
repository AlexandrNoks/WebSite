from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .utils import *


# Create your views here.
class Home(DataMixin, ListView):
    model = Directions
    template_name = "app_test/index.html"
    context_object_name = 'directions'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        nav_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(nav_def.items()))


class ShowDirection(DataMixin, DetailView):
    model = Category
    template_name = "app_test/show.html"
    slug_url_kwarg = "slug_dir"
    context_object_name = "direction"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dir_def = self.get_user_context(title=context["direction"])
        return dict(list(context.items()) + list(dir_def.items()))


class DataForms(DataMixin,CreateView):
    model = MyForm
    template_name = "app_test/test.html"
    fields = ["your_name","your_phone","select_direction"]
    template_name_suffix = "test"

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        get_form = self.get_user_context(title="Моя Форма")
        context_form = dict(list(context.items()) + list(get_form.items()))
        return context_form










# def index(request):
#     return render(request,'app_test/index.html')


# def slug_directions(request,slug_dir):
#     directed = get_object_or_404(Directions, slug=slug_dir)
#     home_link = {
#         "directed": directed,
#         "dir_selected": directed.slug
#     }
#     return render(request, 'app_test/show.html', context=home_link)


def about(request):
    about_text = School.objects.get(id=1)
    context = {
        "text": about_text.about_school
    }
    return render(request, 'app_test/about.html', context=context)


def news(request):
    main_news = {
        "title": "НОВОСТИ"
    }
    return render(request, 'app_test/news.html', context=main_news)


def schedule(request):
    main_schedule = {
        "title": "РАСПИСАНИЕ"
    }
    return render(request, 'app_test/schedule.html', context=main_schedule)


def presentation(request):
    main_presentation = {
        "title": "ВЫСТУПЛЕНИЯ"
    }
    return render(request, 'app_test/presentation.html', context=main_presentation)


def form_feedback(request):
    if request.method == "POST":
        show_form = FormFeedBack(request.POST)
        if show_form.is_valid():
            show_form.save()
            return redirect("post")
    else:
        show_form = FormFeedBack()
    return render(request,'app_test/form.html', context={"form": show_form})


# def form_testfeed(request, your_phone):
#     if request.method == "POST":
#         test_form = FormTestFeed(request.POST)
#         if test_form.is_valid():
#            test_form.save()
#            return redirect("test")
#     else:
#         test_form = FormFeedBack()
#     return render(request,'app_test/test.html', context={"test": test_form})

def form_test(request):
    return render(request, 'app_test/test_out.html')


def post(request):
    return render(request, 'app_test/post.html')


def vk(request):
    return HttpResponse(request,"Hello, VK!")


def wa(request):
    return HttpResponse(request,"Hello, Whats App!")


def tg(request):
    return HttpResponse(request,"Hello, Telegramm!")


def rabbits(request):
    name = request.GET.get('name','Bags')
    id = request.GET.get('id',2)
    return HttpResponse(f'<h2>name: {name}</h2><h1>id: {id}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(request,'<h1>Страница не найдена</h1>')



