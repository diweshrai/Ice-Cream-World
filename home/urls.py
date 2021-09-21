from django.contrib import admin
from django.urls import path
from home import views



admin.site.site_header = "Ice-Cream-World"
admin.site.site_title = "Ice-Cream-world"
admin.site.index_title = "Welcome to Ice-Cream-world  "


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("soft", views.soft, name='soft'),
    path("hard", views.hard, name='hard'),
    path("nosugar", views.nosugar, name='nosugar'),
    path("french", views.french, name='french'),
    path("light", views.light, name='light'),
    path("organic", views.organic, name='organic'),
    path("sign", views.sign, name='sign'),
     path("register", views.register, name='register')


]