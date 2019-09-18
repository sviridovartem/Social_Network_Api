from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from friendship import views

router = SimpleRouter()
router.register(r'', views.FriendshipDetail)

urlpatterns = format_suffix_patterns([
    path('', views.FriendshipList.as_view()),
    # path('<int:pk>/accept_friendship', views.FriendshipDetail.as_view({'get': 'accept_friendship'})),
    # path('<int:pk>/delete_friendship', views.FriendshipDetail.as_view({'get': 'delete_friendship'})),
    path('', include(router.urls)),
])
