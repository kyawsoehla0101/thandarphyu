from django.urls import path
from . import views
urlpatterns = [
    path('',views.heroView, name='hero'),
    path('post/<str:slug>/',views.detailView, name='detail'),
]
