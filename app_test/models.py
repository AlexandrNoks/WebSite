from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    direction = models.CharField(max_length=100, db_index=True, verbose_name="Категории", blank=True)
    slug = models.SlugField(max_length=100, unique=True,db_index=True, verbose_name="URL")

    def __str__(self):
        return f"{self.direction}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["direction"]


class Directions(models.Model):
    price_one_day = models.IntegerField(null=True, verbose_name="Разовое")
    price_ticket = models.IntegerField(null=True, verbose_name="Абонемент")
    text_direction = models.CharField(max_length=10000, verbose_name="Описание")
    location = models.CharField(max_length=1000, verbose_name="Адрес")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    name_direction = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Направление")

    def __str__(self):
        return f"{self.name_direction}"

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
        ordering = ["name_direction"]

    def get_absolute_url(self):
        return reverse("show", kwargs={"slug_dir": self.slug})


class Form(models.Model):
    your_name = models.CharField(max_length=1000)
    regex_phone = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    your_phone = models.CharField(validators=[regex_phone], max_length=16, unique=True)
    select_direction = models.ForeignKey(Directions, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.your_name}"



    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        ordering = ["id"]


class School(models.Model):
    about_school = models.CharField(max_length=100000, verbose_name="О Нас", default="Школа музыки и танца 'MAXIMUM skill' для детей от 3 до 16 лет. Мы находимся по адресам: - СК «Олимпийский» ул. Новая 17; - БЦ Премьер ул. Терешковой 263/2 Школа дополнительного образования «Максимум skill» для детей с 3-х лет, основана в 2018 году. Филиал №1 - имеет следующие направления деятельности: ТАНЦЫ для детей с 3-х лет. Современная хореография, Шаффл, Брейк-данс, растяжка, отличная физ. подготовка. МОДЕЛЬНОЕ МАСТЕРСТВО. Подиум, фотопозирование, фотосьемка. АКТЕРСКОЕ МАСТЕРСТВО. Театр, постановка мюзикла. Филиал №2 – имеет следующие направления деятельности: ЭСТРАДНЫЙ ВОКАЛ, ИГРА НА ГИТАРЕ, МАСТЕР КЛАССЫ ТВОРЧЕСКИЕ ДЛЯ ДЕТЕЙ. МИССИЯ ШКОЛЫ – дать детям все самое ценное, а именно skill – навык, умение, мастерство, искусство, здоровье и развитие личности! Дети получают полноценные занятия, теоретические и практические. В программе обучения: развитие музыкального слуха, развитие чувства ритма, постановка голоса, постановка номеров, запись песен на профессиональной студии звукозаписи. Выступают коллективом на международных конкурсах, городских площадках, а также на отчетных концертах школы.")
    count_teacher = models.IntegerField(null=False, verbose_name="Количество учителей",blank=False)
    count_pupil = models.IntegerField(null=False, verbose_name="Количество учеников",blank=False)
    count_directions = models.IntegerField(null=False, verbose_name="Количество направлений", default="5", blank=False)

    def __str__(self):
        return f"{self.about_school}"

    class Meta:
        verbose_name = "О Школе"
        verbose_name_plural = "О Школе"
        ordering = ["id"]


class MyForm(models.Model):
    your_name = models.CharField(max_length=1000)
    regex_phone = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    your_phone = models.CharField(validators=[regex_phone], max_length=16)
    select_direction = models.ForeignKey(Directions, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.your_name}"

    def get_absolute_url(self):
        return reverse("testout")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        ordering = ["id"]

# class Pupils(models.Model):
#     name_parents = models.CharField(max_length=1000, verbose_name="Имя родителя: ")
#     name_children = models.CharField(max_length=1000, verbose_name="Имя ребенка: ")
#     age_children = models.IntegerField(null=False)
#     phoneNumber = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#     secondPhoneNumber = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#     direction = models.ForeignKey(Directions, on_delete=models.CASCADE, blank=True)
#
#
# class Teachers(models.Model):
#     name_teacher = models.CharField(max_length=1000, verbose_name="Имя учителя: ")
#     description = models.CharField(max_length=1000, verbose_name="Характеристика: ")
#     photo = models.ImageField(upload_to="test_app/img/")
#     direction = models.ForeignKey(Directions, on_delete=models.CASCADE, blank=True)
#
#
class Presentation(models.Model):
    name_presentation = models.CharField(max_length=100, verbose_name="Выступления")
    text = models.CharField(max_length=10000, blank=False, verbose_name="Описание")
    link = models.URLField(max_length=100, verbose_name="Ссылка")
    photo = models.ImageField(upload_to="app_test/photo/", verbose_name="Фото")
    date_publication = models.DateTimeField(auto_now_add=True, verbose_name="Дата мероприятия")
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name_presentation

    class Meta:
        verbose_name = "Выступление"
        verbose_name_plural = "Выступления"
        ordering = ["date_publication"]


    def __str__(self):
        return self.direction

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]

# class News(models.Model):
#     name_post = models.CharField(max_length=100, blank=True)
#     text_post = models.CharField(max_length=10000, unique="", blank=True)
#     photo_post = models.ImageField(unique="",)
#     direction = models.ForeignKey(Directions, on_delete=models.CASCADE, blank=True)


