from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subscription import views

urlpatterns = [
    path('', views.SubscriptionList.as_view()),
    path('<int:pk>/', views.SubscriptionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
