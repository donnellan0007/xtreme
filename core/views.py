from django.shortcuts import render, redirect
from .models import Trip

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def done(request):
    return render(request,'core/complete.html')

def purchase(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        Trip.objects.create(buyer=name, email=email, date=date)
        context = {
            'name': name,
            'email': email,
            'date': date
        }
        return render(request, 'core/success.html', context)
    return render(request, 'core/buy.html')