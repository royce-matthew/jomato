from django.conf.urls import url
from jsec import views

urlpatterns = [
    url(r'^stalls/$', views.stall_list),
    url(r'^stalls/(?P<pk>[0-9]+)/$', views.stall_detail),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.stall_reviews),
    url(r'^reviews/$', views.review_list),
    url(r'^view/$', views.single),
    url(r'^$', views.index),
]