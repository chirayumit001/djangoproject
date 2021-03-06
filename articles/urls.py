from django.conf.urls import url
from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^create/$', views.article_create, name='create'),
    #personal
    url(r'^article_my/$', views.article_my, name='article_my'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail')
]