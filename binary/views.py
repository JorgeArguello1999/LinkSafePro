from django.shortcuts import render

def get(request):
    return render(request, 'binary.html')