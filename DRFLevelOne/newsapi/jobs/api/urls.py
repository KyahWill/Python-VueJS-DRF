from django.urls import path
from jobs.api.views import JobOfferDetailAPIView,JobOfferCreateAPIView
# from news.api.views import article_list_create_api_view,article_detail_api_view


urlpatterns = [
    path("jobs/",JobOfferCreateAPIView.as_view(),name = 'job-list'),
    path("jobs/<int:pk>/",JobOfferDetailAPIView.as_view(),name ='job-detail'),
    # path("articles/",article_list_create_api_view,name = 'article-list'),
    # path("articles/<int:pk>/",article_detail_api_view,name ='article-detail'),
    
]