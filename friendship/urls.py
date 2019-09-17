from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from friendship import views

router = SimpleRouter()
router.register(r'friends', views.FriendshipDetail)

urlpatterns = format_suffix_patterns([
    path('', views.FriendshipList.as_view()),
    # path('<int:pk>/', views.FriendshipDetail.as_view({'get': 'accept_friendship'})),
    path('<int:pk>/', views.FriendshipDetail.as_view({'get': 'accept_friendship'})),
    # path('users/<int:pk>/', views.FriendshipDetail.perform_update(), name='accept-friendship')
    path('', include(router.urls)),
])
