from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})

def create(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['email'] and request.POST['message']:
            contact = Contact()
            contact.name = request.POST['name']
            contact.email = request.POST['email']
            contact.message = request.POST['message']
            contact.save()
            return redirect('home')
        else:
            return render(request, 'index.html', {'error': 'All fields are mandatory'})
    else:
        return render(request, 'index.html')


    