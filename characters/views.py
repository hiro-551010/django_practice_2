from django.shortcuts import render
from .forms import CharactersModelForm
from django.views.generic import TemplateView, DetailView
from .models import Characters
from .tables import CharactersTable
from django_tables2 import SingleTableView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    return render(request, 'characters/index.html')
    
"""
def signup(request):
    form = CharactersForm()
    if request.method == 'POST':
        form = CharactersForm(request.POST)
        if form.is_valid():
            print('バリデーション成功')
            print(f"name: {form.cleaned_data['name']}, gender: {form.cleaned_data['gender']}, discription: {form.cleaned_data['discription']}")

    return render(request, 'characters/signup.html', context={'form': form})
"""

@login_required
def chara(request):
    form = CharactersModelForm()
    if request.method == 'POST':
        form = CharactersModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            print('エラーがありました')
    return render(request, 'characters/form_model.html', context = {'form': form})

        


class CharaList(LoginRequiredMixin, TemplateView):
    model = Characters
    template_name = 'characters/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characters'] = Characters.objects.all()
        return context

class CharaTable(LoginRequiredMixin, SingleTableView):
    table_class = CharactersTable
    template_name = 'characters/table.html'
    queryset = Characters.objects.all()

    def get_queryset(self):
        query = super().get_queryset()
        character_name = self.request.GET.get('name')
        character_gender = self.request.GET.get('gender')
        if character_name:
            query = query.filter(name=character_name)
            print(query, 'name')
            return query
        if character_gender:
            query = query.filter(gender=character_gender)
            print(query, 'gender')
            return query
        return query


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = Characters.objects.all()
        return context
