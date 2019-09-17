from django.contrib import admin
from django.urls import include, path
from group import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('admin/', admin.site.urls),
    path('friendship/', include('friendship.urls')),
    path('group/', include('group.urls')),
    path('news/', include('news.urls')),
    path('subscription/', include('subscription.urls')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
