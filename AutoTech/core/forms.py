from django.forms import ModelForm
from .models import *

class b_dataForm(ModelForm):
    class Meta:
        model = b_data
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(b_dataForm, self).__init__(*args, **kwargs)
        # Dictionary mapping field names to their custom labels
        custom_labels = {
            'RK': 'Номер на работна карта',
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
            'R_DATA': 'Текуща дата',
            # Add all fields here
        }
        for field_name, field in self.fields.items():
            field.required = True
            if field_name in custom_labels:
                field.label = custom_labels[field_name]
        
class c_dataForm(ModelForm):
    class Meta:
        model = c_data
        fields = ['ime', 'telefon']
    
    def __init__(self, *args, **kwargs):
        super(c_dataForm, self).__init__(*args, **kwargs)
        # Dictionary mapping field names to their custom labels
        custom_labels = {
            'ime': 'Име на клиента',
            'telefon': 'Телефон за връзка',
            # Add all fields here
        }
        for field_name, field in self.fields.items():
            field.required = True
            if field_name in custom_labels:
                field.label = custom_labels[field_name]
                
class w_dataForm(ModelForm):
    class Meta:
        model = w_data
        fields = '__all__'
                
class p_dataForm(ModelForm):
    class Meta:
        model = p_data
        fields = '__all__'