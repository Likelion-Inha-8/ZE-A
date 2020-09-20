"""firstsite URL Configuration

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
import hello.views
import account.views
import apply.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.main, name='main'),
    path('home', hello.views.home, name='home'),
    path('detail/<int:post_id>', hello.views.detail,name="detail"),
    path('edit/<int:post_id>', hello.views.postedit,name="postedit"),
    path('postupdate/<int:post_id>', hello.views.postupdate,name="postupdate"),
    path('postdelete/<int:post_id>', hello.views.postdelete,name="postdelete"),
    path('postnew', hello.views.postnew, name='postnew'),
    path('postcreate', hello.views.postcreate, name='postcreate'),
    path('login/', account.views.login, name='login'),
    path('signup00/', account.views.signup00, name='signup00'),
    path('signup01/', account.views.signup01, name='signup01'),
    path('signup02/', account.views.signup02, name='signup02'),
    path('logout/', account.views.logout, name="logout"),
    path('apply1/', hello.views.apply1, name="apply1"),
    path('merchandiserApply/',apply.views.merchandiserApply, name = "merchandiserApply" ),
    path('merchandiserApplyTry/', apply.views.merchandiserApplyTry, name = "merchandiserApplyTry"),
    path('studentApply/', apply.views.studentApply, name = "studentApply"),
    path('studentApplyTry/', apply.views.studentApplyTry, name = "studentApplyTry"),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
