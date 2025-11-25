from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_dark/', views.index_dark, name='index_dark'),
    path('', views.intro, name='intro'),
    path('contactus/'  , views.ContactUsView.as_view(), name='contactus'),
]