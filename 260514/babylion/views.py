from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lions(request):
    context = { 'lions': '도한' }
    return render(request, 'lions.html', context)