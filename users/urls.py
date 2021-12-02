from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_users, name='all_users'),
    path('all_users/ajax', views.friend_add, name='ajax_add_friend'),
    path('index/add/ajax', views.friend_add_index, name='ajax_index_add'),
    path('index/no_add/ajax', views.friend_no_add_index, name='ajax_index_no_add'),
    path('index/no_friend/ajax',views.friend_no_index, name='ajax_no_friend'),
    path('index/dont_like/ajax', views.dont_like, name='dont_like'),
    path('index/exit/ajax', views.exit, name='ajax_exit'),
    path('account/<str:user_name>', views.user, name='users'),
    path('login', views.login, name='users_log'),
    path('sigin', views.sigin, name='users_sigin'),
]
