from django.urls import path
from .views import HomePageview

urlpatterns = [
    path('', HomePageview, name='home'),
]
#localhost:8000/admin/