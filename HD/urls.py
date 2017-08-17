from django.conf.urls import url
from HD import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^datasub/$', views.submit_data, name='datasub'),
    url(r'^dataview/$', views.view_data, name='dataview'),
            ]