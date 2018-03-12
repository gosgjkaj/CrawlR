from django.conf.urls import url
from CrawlR import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^popular/$', views.popular, name = 'popular'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category'),
    url(r'^register/$', views.register, name= 'register'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),

    ]
