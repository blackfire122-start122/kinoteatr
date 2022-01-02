from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/ajax', views.like_ajax, name='like_ajax'),
    path('comment/ajax', views.comment_ajax, name='comment_ajax'),
    path('comment_delete/ajax', views.comment_delete_ajax, name='comment_delete_ajax'),
    path('about', views.about, name='about'),
    path('about/autor', views.autor, name='autor'),
    path('type/<str:str_url_type>/genre/<str:str_url_genre>/year/<str:str_year>', views.tg, name='tg'),
    path('film/<str:typef>/<int:fn>/', views.film, name='film'),
    path('film/stream/<str:typef>/<int:pk>/', views.get_streaming_video, name='stream'),
]
