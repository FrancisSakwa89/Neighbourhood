from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.core.urlresolvers import reverse
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^search/', views.search,name = 'search'),
    url(r'^new/neighbourhood$',views.newneighbourhood, name='newneighbourhood'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^neighbourhood/(\d+)', views.neighbourhood, name='neighbourhood'),
    url(r'^new/business/',views.newbusiness, name='newbusiness'), 
    url(r'^new/profile$',views.newprofile, name='newprofile'),
    url(r'^new/comment$',views.newcomment, name='newcomment'), 
    url(r'^new/post$',views.newpost, name='newpost'),
    url(r'^mail$',views.mail,name='mail'),
    url(r'^chat/', views.chat, name='chat'),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^business$', views.business,name = 'business'),
    url(r'^myneighbourhood/', views.myneighbourhood, name='myneighbourhood'),
    url(r'^password/', views.password, name='password'),
    url(r'^new/contacts/',views.newcontacts, name='newcontacts'), 
    url(r'^post/(\d+)', views.post, name='post'),
    url(r'^mypost/', views.mypost, name='mypost'),
    url(r'^comments/', views.comments, name='comments'),


]    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
