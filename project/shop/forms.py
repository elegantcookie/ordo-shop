from django import forms
from .models import Product


choices = [
    (0, 'Сортировка'),
    (1, 'Цена по возрастанию'),
    (2, 'Цена по убыванию'),
    (3, 'Порядок А-Я'),
    (4, 'Порядок Я-А')
]


class SortForm(forms.Form):
    gte = forms.IntegerField(min_value=0, label='От', widget=forms.NumberInput(), required=False)
    lte = forms.IntegerField(min_value=0, label='До', widget=forms.NumberInput(), required=False)
    sort = forms.TypedChoiceField(label='',
                                  choices=choices,
                                  widget=forms.Select(
                                    attrs={
                                        'class': 'select-form',
                                        'align': 'center',
                                    }
                                  ), required=False)

# class PriceForm(forms.Form):
#     gte = forms.IntegerField(min_value=0, label='От', widget=forms.NumberInput(), required=False)
#     lte = forms.IntegerField(min_value=0, label='До', widget=forms.NumberInput, required=False)


