from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from friendship import views

router = SimpleRouter()
router.register(r'', views.FriendshipDetail)

urlpatterns = format_suffix_patterns([
    path('', views.FriendshipList.as_view()),
    path('', include(router.urls)),
])
