from . import views
from django.conf.urls import url


urlpatterns=[
    url(r'^$', views.index, name='homepage'),
    url(r'^profile/$', views.myProfile, name='profile'),
    url(r'^search/$', views.search_title, name='search_title'),
    url(r'^details/(\d+)$', views.details, name='details'),
]


# review/(?P<id>\d+)/$
