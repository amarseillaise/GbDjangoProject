"""
URL configuration for GbDjangoProject project.

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

import blog.views
import lesson1_2app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coin/<int:n>', lesson1_2app.views.coin, name='coin'),
    path('cube/<int:n>', lesson1_2app.views.cube, name='cube'),
    path('number/<int:n>', lesson1_2app.views.number, name='number'),
    path('statistic/', lesson1_2app.views.statistic, name='statistic'),
    path('authors_list/<int:author_id>', blog.views.authors_list, name='authors-list'),
]
