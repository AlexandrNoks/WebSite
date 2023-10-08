from django.core.exceptions import ValidationError
from django import forms
from .models import *


class FormFeedBack(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["select_direction"].empty_label = "Категория не выбрана"

    class Meta:
        model = Form
        fields = "__all__"


class FormTestFeed(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["select_direction"].empty_label = "Категория не выбрана"

    class Meta:
        model = MyForm
        fields = "__all__"

