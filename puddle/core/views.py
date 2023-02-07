from django.shortcuts import render

def index(request):
    return render(request, "core/index.html") 

def contact(request):
    # Links to the contact page
    return render(request, "core/contact.html")