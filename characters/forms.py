from django import forms
from .models import Characters

"""
class CharactersForm(forms.Form):
    name = forms.CharField(label='名前', max_length=20)
    gender = forms.ChoiceField(label='性別', widget=forms.RadioSelect,
        choices = (
            ('unknown', '不明'),
            ('man', '男'),
            ('woman', '女'),
        )
    )  
    discription = forms.CharField(label="説明", max_length=1000)
"""


class CharactersModelForm(forms.ModelForm):

    class Meta:
        model = Characters
        fields = ('name', 'gender', 'discription', 'image')





