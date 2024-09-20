"""
URL configuration for OnePage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from OnePage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about),
    path('couses/<uid>', views.couses,name='couses2'),
    path('user/',views.userform),
    path('cal/',views.calculator,name='cd'),
    path('book/',views.bookpage),
    path('name/',views.namepage),
    path('save/',views.savepage, name='savepage'),
    path('contact/',views.contactform,name='contact'),
    path('contactpage/',views.cotactdata,name="contactpage1"),
]

if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# urlpatterns = [
#     # your URL patterns...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
