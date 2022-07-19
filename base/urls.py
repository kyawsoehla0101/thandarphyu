from django.urls import path
from . import views
urlpatterns = [
    path('',views.homeView, name='home'),
    path('post/<str:slug>/',views.detailView, name='detail'),
    path('gallery/',views.galleryView,name='gallery'),
    path('about-me/',views.aboutView,name='about'),
    path('contact-me/',views.contactView,name='contact'),
    path('tag/<str:slug>/', views.tagView,name='tag' ),
    path('category/<str:slug>/', views.categoryView,name='category' ),
]
