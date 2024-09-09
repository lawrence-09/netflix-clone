from django.urls import path 
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name="login"),
    path('genre/<str:pk>/', views.genre, name='genre'),
    path('movie/<str:pk>/',views.movie, name='movie'),
    path('my-list',views.my_list, name='my-list'),
    path('search',views.search,name='search'),
    path('logout',views.logout,name='logout'),
    path('add-to-list', views.add_to_list,name='add-to-list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)