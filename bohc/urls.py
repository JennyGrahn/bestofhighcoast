"""
URL configuration for bohc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.about, name='about'),
    path('', myapp_views.card, name='destinations'),
    path('', myapp_views.favourites, name='favourite lists'),
    path('', myapp_views.mbrpages, name='member pages'),
    path('', myapp_views.signin, name='sign in'),
    path('', myapp_views.submitplc, name='submit a new destination'),
    path('', myapp_views.index, name='home'),
    
]
