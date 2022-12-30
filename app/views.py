from django.shortcuts import render

# Create your views here.
def twitter(request):
    return render(request,'twitter.html')

def bunny(request):
    return render(request,'bunny.html')