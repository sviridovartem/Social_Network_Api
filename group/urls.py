from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from group import views

urlpatterns = [
    path('', views.GroupList.as_view()),
    path('<int:pk>/', views.GroupDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
