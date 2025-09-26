from django.shortcuts import render, redirect
from .models import Alert
from .forms import AlertForm

def index(request):
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlertForm()

    return render(request, 'alerts/index.html', {'form': form})