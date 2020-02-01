from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns= [
    path('relative/',views.relative, name='relative'),
    path('other/',views.other, name='other'),
]
