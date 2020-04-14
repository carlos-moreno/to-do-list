"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import todolist.core.views

urlpatterns = [
    path("", todolist.core.views.list, name="list"),
    path("new", todolist.core.views.new, name="new"),
    path("detail/<slug:slug>/", todolist.core.views.detail, name="detail"),
    path("delete/<slug:slug>/", todolist.core.views.delete, name="delete"),
    path("admin/", admin.site.urls),
]
