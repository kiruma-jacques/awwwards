from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$', views.index, name='homepage'),
    url(r'^profile/$', views.myProfile, name='profile'),
    url(r'^review/$', views.review, name='review'),
]
