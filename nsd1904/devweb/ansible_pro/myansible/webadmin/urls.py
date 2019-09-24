from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'', views.index, name='polls_index'),
]