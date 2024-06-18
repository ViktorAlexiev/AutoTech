from django.forms import ModelForm
from django import forms
from .models import *

class b_dataForm(ModelForm):
    class Meta:
        model = b_data
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(b_dataForm, self).__init__(*args, **kwargs)
        custom_labels = {
            'RK': 'Номер на сервизна карта',
            'RN': 'Регистрационен номер',
            'Marka': 'Марка',
            'Model': 'Модел',
            'G_PR': 'Година на производство',
            'KM': 'Изминати километри',
            'Rama': 'Рама',
            'Kupe': 'Купе',
            'Dvigatel': 'Двигател',
            'Descr': 'Описание на автомобила',
            'Problem': 'Проблем на автомобила',
            'R_DATA': 'Дата на издаване',
        }
        for field_name, field in self.fields.items():
            field.required = True
            if field_name in custom_labels:
                field.label = custom_labels[field_name]
            self.fields['RK'].widget.attrs['readonly'] = True
        
class c_dataForm(ModelForm):
    class Meta:
        model = c_data
        fields = ['ime', 'telefon']
    
    def __init__(self, *args, **kwargs):
        super(c_dataForm, self).__init__(*args, **kwargs)
        custom_labels = {
            'ime': 'Име на клиента',
            'telefon': 'Телефон за връзка',
        }
        for field_name, field in self.fields.items():
            field.required = True
            if field_name in custom_labels:
                field.label = custom_labels[field_name]
                
class searchForm(forms.Form):
    RN = forms.CharField(max_length=255, required=False, label="Регистрационен номер")
    ime = forms.CharField(max_length=255, required=False, label="Име на клиента")
    date1 = forms.DateField(required=False, label="От дата1")
    date2 = forms.DateField(required=False, label="До дата2")
                
class w_dataForm(ModelForm):
    class Meta:
        model = w_data
        fields = '__all__'
                
class p_dataForm(ModelForm):
    class Meta:
        model = p_data
        fields = '__all__'