from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$', views.about),
    url(r'^$', article_views.article_list, name='home'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
