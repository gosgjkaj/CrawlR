from django.conf.urls import url
from Crawlr import views

app_name = 'Crawlr'
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<route_name_slug>[\w\-]+)', views.show_route, name = 'show_route'),
    url(r'^register/$', views.register, name= 'register'),
    #url(r'^profile/', views.profile, name='profile'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_route/$', views.add_route, name='add_route'),
    url(r'^popular/$', views.popular, name="popular"),

]
