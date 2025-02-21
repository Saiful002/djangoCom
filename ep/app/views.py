from django.shortcuts import render

def home(request):
    # Your home view logic
    return render(request, 'app/home.html')

def about(request):
    # Your about view logic
    return render(request, 'app/about.html')

def contact(request):
    # Your contact view logic
    return render(request, 'app/contact.html')