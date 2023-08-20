"""
URL configuration for start project.

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
from django.urls import path,include
from . import views
urlpatterns = [
    path("admin/login",views.login_view,name='login'),
     path("admin/logout",views.logout_view,name='logout'),
    path("admin/forgot_password",views.forgot_pass,name='forgot_password'),
    # path("admin/send_email",views.send_reset_email_view,name="send_mail"),
    path("admin/password_reset/<uidb64>/<token>",views.password_reset,name="password_reset"),
    path('first_app/',include('first_app.urls',namespace="first_app")),
    path("",views.main_page,name="first_page"),
    path('admin/', admin.site.urls),
 
]
