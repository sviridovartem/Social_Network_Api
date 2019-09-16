from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('friendship/', include('friendship.urls')),
    path('group/', include('group.urls')),
    path('news/', include('news.urls')),
    path('subscription/', include('subscription.urls')),
]
