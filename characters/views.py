from django.shortcuts import render
from .forms import CharactersForm, CharactersModelForm
from django.views.generic import TemplateView
from .models import Characters
from .tables import CharactersTable
from django_tables2 import SingleTableView

def index(request):
    return render(request, 'characters/index.html')
    
def signup(request):
    form = CharactersForm()
    if request.method == 'POST':
        form = CharactersForm(request.POST)
        if form.is_valid():
            print('バリデーション成功')
            print(f"name: {form.cleaned_data['name']}, gender: {form.cleaned_data['gender']}, discription: {form.cleaned_data['discription']}")

    context = {
        'form': form,
    }
    return render(request, 'characters/signup.html', context)

def chara(request):
    form = CharactersModelForm()
    if request.method == 'POST':
        form = CharactersModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('エラーがありました')
    return render(request, 'characters/form_model.html', context = {'form': form})

        


class CharaList(TemplateView):
    model = Characters
    template_name = 'characters/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characters'] = Characters.objects.all()
        return context

class CharaTable(SingleTableView):
    table_class = CharactersTable(Characters)
    template_name = 'characters/table.html'
    
    def get_queryset(self):
        return Characters.objects.all()