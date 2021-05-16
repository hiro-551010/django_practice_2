from django.contrib import admin
from .forms import CharactersModelForm
from .models import Characters



admin.site.register(Characters)
