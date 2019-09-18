from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news import views

urlpatterns = [
    path('', views.NewsList.as_view()),
    path('<int:pk>/', views.NewsDetail.as_view()),
    path('users_news/', views.UserNewsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
