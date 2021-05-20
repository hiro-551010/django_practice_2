import django_tables2 as tables
from .models import Characters

class CharactersTable(tables.Table):
    name = tables.Column(verbose_name='名前')
    gender = tables.Column(verbose_name='性別')
    discription = tables.Column(verbose_name='特徴')


    class Meta:
        model = Characters
        tamplate_name = 'characters/table.html'
        fields = ('name', 'gender', 'discription', 'image')

from django.utils.html import format_html


