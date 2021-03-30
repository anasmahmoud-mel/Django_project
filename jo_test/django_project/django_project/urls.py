"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from firstOne.views import index ,chart, activity
from firstOne.views import indexForm
from firstOne.views import indexTable
from register.views import register
from firstOne.views import handler404
from django.conf.urls import url
from firstOne.views import simple_upload
from firstOne import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register),
    path('', include("django.contrib.auth.urls")),
    path('', register),

    path('index/', views.chart, name='index'),
     # path('form/', indexForm),

    url('^$', index, name='home'),

    # add excel sheet (upload data)
    path('upload/', simple_upload, name='upload'),
    # CRUD URL


    path('show', views.show),
    path('table/', views.show, name='table'),

    path('new', views.new, name='new'),

    path('add', views.add),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),

    path('search', views.search, name='search'),

    path('activity/', views.activity, name='activity'),



    # path('anas', views.header),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('../assets/images/icon/logo.png')))
]

handler404 = 'firstOne.views.handler404'
