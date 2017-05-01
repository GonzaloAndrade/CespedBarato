from django.conf.urls import include, url
from django.contrib import admin
from Home import views

urlpatterns = [
    url(r'^$', include('Home.urls', namespace="home")),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]