from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("blog/<int:pk>", blog, name="blog"),
    path("blogs", blogMain, name="blogs"),
    path("service", service, name="service"),
    path("scrapbook", scrapbook, name="scrapbook"),
    path("gallery/<int:pk>", Gallery, name="Gallery"),
    path('comment/<int:pk>', comment, name='comment'),
    path('subscribe/', subscribe, name='subscribe'), 
    path('services', service, name='services'),
    path('blog-settings', blogsettingsview, name='blog-settings'),
    path("like_post/<int:pk>", LikeView, name="like_post"),
    path('team', team, name='team'),
    path('error404', error404, name='error404'),
    path('privacy-policy', privacyPolicy, name='privacy-policy'),
]
    