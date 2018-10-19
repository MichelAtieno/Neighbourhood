from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^createHood/$', views.hood, name='createHood'),
    url(r'^myHoods/$',views.GetHood, name = 'myHood'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^join/(\d+)',views.joinHood, name = 'joinHood'),
    url(r'^exitHood/(\d+)',views.exitHood, name = 'exitHood'),
    url(r'^search/$',views.search, name= 'search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)