from django.shortcuts import render, redirect

# Create your views here.

from .forms import CalculationForm
from .models import Calculation


def index(request):
    if request.method == 'POST':
            form = CalculationForm(request.POST)
            if form.is_valid():
               instance = form.save(commit= False)
               instance.result = instance.principle*(instance.rate/100)*instance.time
               instance.save()
               return redirect('index')
    else:
         form = CalculationForm()  
    Calculations = Calculation.objects.all().order_by      
    return render(request, 'index.html', {'form': form, 'calculations': Calculations})
    
