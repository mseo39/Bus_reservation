"""bus_reservation URL Configuration

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
from django.urls import path
import main.views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chk',main.views.chk,name="chk"),
    path('chk_cancel',main.views.chk_cancel,name="chk_cancel"),
    path('select_date',main.views.select_date,name="select_date"),
    path('cancel_date',main.views.cancel_date,name="cancel_date"),
    path('date',main.views.date,name="date"),

    path('signup/', main.views.signup, name="signup"),
    path('login/', main.views.login, name="login"),
    path('logout/', LogoutView.as_view(next_page='date'), name="logout"),

    path('mypage',main.views.mypage, name="mypage"),
]
