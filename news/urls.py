from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news import views

urlpatterns = [
    path('', views.NewsList.as_view()),
    path('<int:pk>/', views.NewsDetail.as_view()),

    # Get news for user
    # Get news of the groups that I’m subscribed to (has filters by date from and to

]

urlpatterns = format_suffix_patterns(urlpatterns)
