from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from group import views

router = SimpleRouter()
router.register(r'', views.GroupDetail)

urlpatterns = [
    path('', views.GroupList.as_view()),
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
