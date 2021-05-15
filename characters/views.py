from django.shortcuts import render
from .forms import CharactersForm

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

def list(request):
    return render(request, 'characters/list.html')
