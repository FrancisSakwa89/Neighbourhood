from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^new/neighbourhood$',views.newneighbourhood, name='newneighbourhood'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^neighbourhood/(\d+)', views.neighbourhood, name='neighbourhood'),
    url(r'^new/business/',views.newbusiness, name='newbusiness'), 
    url(r'^new/profile$',views.newprofile, name='newprofile'),
    url(r'^new/comment$',views.newcomment, name='newcomment'), 
    url(r'^new/post$',views.newpost, name='newpost'),
    url(r'^mail$',views.mail,name='mail'),
    # url(r'^api/business/$', views.BusinessList.as_view()),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^business$', views.business,name = 'business'),
    url(r'^myneighbourhood/', views.myneighbourhood, name='myneighbourhood'),
    url(r'^password/', views.password, name='password'),


]    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
