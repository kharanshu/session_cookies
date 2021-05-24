"""cookies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scookie/',views.set_cookie, name='sc'),
    path('gcookie/',views.get_cookie, name='gc'),
    path('dcookie/',views.del_cookie, name='dc'),
    path('home/',views.homepage, name='home'),
    path('testcookie/', views.cookie_session),
    path('deletecookie/', views.cookie_delete),
    path('demo-view/', views.demo_view),

    path('create/', views.create_session),
    path('delete/', views.delete_session),

    path('show-session/', views.show_session_data),
]
