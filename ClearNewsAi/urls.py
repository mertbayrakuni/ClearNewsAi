from django.urls import path
from .views import demo_page

urlpatterns = [
    path('', demo_page, name='home'),
]
