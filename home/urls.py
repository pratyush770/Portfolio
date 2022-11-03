from django.contrib import admin
from django.urls import path
from home import views

#Django admin customization
admin.site.site_title="Portfolio"
admin.site.site_header="Login to your admin"
admin.site.index_title="Welcome to this portal"
urlpatterns = [
     path('', views.home, name='home'),
     path('about', views.about, name='about'),
     path('projects', views.projects, name='projects'),
     path('contact/', views.contact, name='contact'),
]