from django.conf.urls import url
from crawlr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
     url(r'^route/(?P<route_name_slug>[\w\-]+)/$',
        views.show_route, name='show_route'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_route/$',
        views.add_route, name='add_route'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^save_route/$', views.add_route, name='add_route'),
    url(r'^find_directions/$', views.find_directions, name='find_directions'),
    url(r'^like/$', views.like_route, name='like_route'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)/$', views.show_profile, name='show_profile'),
    url(r'^profile/$', views.show_profile, name='show_profile'),
]
