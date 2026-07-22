from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus/'  , views.ContactUsView.as_view(), name='contactus'),
]