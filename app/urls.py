from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^createHood/$', views.hood, name='createHood'),
    url(r'^myHoods/$',views.GetHood, name = 'myHood'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^join/(\d+)',views.joinHood, name = 'joinHood'),
    url(r'^exitHood/(\d+)',views.exitHood, name = 'exitHood'),
    url(r'^search/$',views.search, name= 'search'),
    url(r'^hoodPost/$',views.hoodPost, name = 'hoodPost'),
    url(r'^singlePost/(\d+)',views.singlePost, name = 'singlePost'),
    url(r'^allPosts/$',views.allPosts,name = 'allPosts'),
    url(r'^business/$',views.getBusiness, name= 'business'),
    url(r'^createBusiness/$',views.business, name= 'createBusiness'),
    url(r'^searchBusiness/$',views.search_business,name = 'searchBusiness'),
    url(r'^editProfile/$',views.editProfile,name= 'editProfile'),
    url(r'^editBusiness/(\d+)',views.editBusiness,name = 'editBusiness'),
    url(r'^deletePost/(\d+)',views.deletePost,name = 'deletePost'),
    url(r'^deleteBusiness/(\d+)',views.deleteBusiness,name = 'deleteBusiness'),
    url(r'^deleteHood/(\d+)',views.deleteHood,name = 'deleteHood'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)