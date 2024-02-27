
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('getdata', views.GetData, name='getdata'),
    path('edit/<int:id>', views.DataEdit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
]
