"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from rango import views

from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static
# serve content from the media directory of project from the /media/URL


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.user_login, name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#tell Django to serve static content from MEDIA_URL
# project’s settings.py module, you will notice that one of the preinstalled apps (within the INSTALLED_APPS list) is django.contrib.admin