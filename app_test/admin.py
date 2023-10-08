from django.contrib import admin
from .models import *


# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ('id','direction',)
    list_display_link = ('id','direction')
    search_fields = ('direction',)
    prepopulated_fields = {"slug": ("direction",)}


class AdminDirections(admin.ModelAdmin):
    list_display = ('id','name_direction',)
    list_display_link = ('id','name_direction',)
    search_fields = ('name_direction',)
    prepopulated_fields = {"slug": ("name_direction",)}


class AdminForm(admin.ModelAdmin):
    list_display = ('id','your_name','your_phone','select_direction')
    list_display_link = ('id','your_name','your_phone','select_direction')
    list_filter = ('id',)
    search_fields = ('your_name',' regex_phone','your_phone','select_direction')


class AdminSchool(admin.ModelAdmin):
    list_display = ('id','about_school','count_teacher','count_pupil','count_directions')
    list_display_link = ('id','about_school','count_teacher','count_pupil','count_directions')
    list_filter = ('id',)
    search_fields = ('about_school','count_teacher','count_pupil','count_directions')


class AdminPresentation(admin.ModelAdmin):
    list_display = ('id','name_presentation','text','link','photo','date_publication','direction')
    list_display_link = ('id','name_presentation','text','link','photo','date_publication','direction')
    list_filter = ('date_publication',)
    search_fields = ('name_presentation','text','link','photo','date_publication','direction')


class AdminMyForm(admin.ModelAdmin):
    list_display = ('id','your_name','your_phone','select_direction')
    list_display_link = ('id','your_name','your_phone','select_direction')
    list_filter = ('id',)
    search_fields = ('your_name',' regex_phone','your_phone','select_direction')


admin.site.register(Category, AdminCategory)
admin.site.register(Directions, AdminDirections)
admin.site.register(Form, AdminForm)
admin.site.register(School, AdminSchool)
admin.site.register(Presentation, AdminPresentation)
admin.site.register(MyForm, AdminMyForm)

# admin.site.register(PriceSchool)
# admin.site.register(DirectionGroup)
# admin.site.register(AddDate)
# admin.site.register(AddPupil)
# admin.site.register(PupilGroup,AdminModelGroup)


