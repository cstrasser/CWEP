from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = (
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'about/$', 'main.views.about', name='about'),
    url(r'^sto/', include('sto.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
