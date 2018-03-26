from django.conf.urls import url
from crawlr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
     url(r'^route/(?P<route_name_slug>[\w\-]+)/$',
        views.show_route, name='show_route'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_route/$',
        views.add_route, name='add_route'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^save_route/$', views.add_route, name='add_route'),
    url(r'^find_directions/$', views.find_directions, name='find_directions'),
]
