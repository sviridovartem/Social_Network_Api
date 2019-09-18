from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from subscription import views

router = SimpleRouter()
router.register(r'', views.SubscriptionDetail)

urlpatterns = [
    path('', views.SubscriptionList.as_view()),
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
