from django.shortcuts import render, redirect
from .models import Image
from .forms import AddImageForm


def dashboard(request):
    images = Image.objects.all()
    return render(request, 'dashboard.html', {'images':images})

def add_image(request):
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
          form =  AddImageForm()
    return render(request, 'add_image.html', {'form':form})


