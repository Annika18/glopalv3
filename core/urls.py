
from django.conf.urls import url
from . import views

urlpatterns = [
    # /core/

    url(r'^$', views.index, name='index'),

    # /core/712/
    url(r'^(?P<activity_id>[0-9]+)/$', views.detail, name='detail'),
]