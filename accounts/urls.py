from django.urls import path
from .views import SinnUpView

urlpatterns = [
    path('singup',SinnUpView.as_view(),name = 'singup')
]