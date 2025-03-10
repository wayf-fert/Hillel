from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Кореневий URL
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # Динамічні URL-шляхи
    re_path(r'^post/(?P<id>\d+)/$', views.post_view, name='post'),  # Числовий ID
    re_path(r'^profile/(?P<username>[a-zA-Z]+)/$', views.profile_view, name='profile'),  # Літери
    re_path(r'^event/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.event_view, name='event'),  # Дата
]