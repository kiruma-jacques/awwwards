from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$', views.index, name='homepage'),
    url(r'^profile/$', views.myProfile, name='profile'),
    url(r'^<int:project_id>/review/$', views.review, name='review'),
]


# review/(?P<id>\d+)/$
