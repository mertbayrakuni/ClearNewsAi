from django.shortcuts import render

def demo_page(request):
    return render(request, 'DemoPage.html')