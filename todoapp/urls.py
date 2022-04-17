"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import TodoItemListView,TodoItemCreateView,TodoItemUpdateView,TodoItemDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/list',TodoItemListView.as_view(),name ='todo_list'),
    path('todo/create',TodoItemCreateView.as_view(),name ='create_list'),
    path('todo/update/<pk>',TodoItemUpdateView.as_view(),name ='update_list'),
    path('todo/delete/<pk>',TodoItemDeleteView.as_view(),name ='delete_list'),

   
]
