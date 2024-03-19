
from django.shortcuts import render

def first_page(request):
    return render(request, 'first_page.html')

def second_page(request):
    return render(request, 'second_page.html')

def third_page(request):
    return render(request, 'third_page.html')

def fourth_page(request):
    return render(request, 'fourth_page.html')

def fifth_page(request):
    return render(request, 'fifth_page.html')
# Create your views here.
