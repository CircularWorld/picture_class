"""tile_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include # wdb

from tile_server import views

urlpatterns  = [
    path('admin/', admin.site.urls),
    # path('', include('fruit_infer.urls')), # wdb
    path('fruit_infer/', include('fruit_infer.urls')), # wdb
    # path('tile_infer/', include('tile_infer.urls')), # wdb
    # path('tile/', include('tile_infer.urls')), #
    path('index/',views.showindex)
]
