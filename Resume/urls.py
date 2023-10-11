from django.urls import path

urlpatterns = [
    path('home', views.home, name='home'),
    path('info', views.info, name='info')
]