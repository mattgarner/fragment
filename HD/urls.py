from django.conf.urls import url
from HD import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^datasub/$', views.submit_data, name='datasub'),
    url(r'^dataview/$', views.view_data, name='dataview'),
    url(r'^worksheets/$', views.worksheet_list, name='worksheet_list'),
    url(r'^wells/$', views.well_list, name='well_list'),
    url(r'^worksheet/(?P<ws_number_slug>[\w\-]+)$', views.show_worksheet, name='show_worksheet'),
    url(r'^worksheet/(?P<ws_number_slug>[\w\-]+)/(?P<well_name>[\w\-]+)$', views.show_well, name='show_well'),
            ]