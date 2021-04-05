from django.shortcuts import render

# Create your views here.e
def demo(request):
    return render(request,'app1_sample.html')
