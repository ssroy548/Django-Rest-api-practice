from django.urls import path
# from .views import article_list_create_api_view, article_detail_api_view
from .views import ArticleListCreateApi, ArticleDetailView

urlpatterns = [
    # path("articles/", article_list_create_api_view, name = "article-list"),
    # path("articles/<int:pk>", article_detail_api_view, name = "article-detail"),
    path("articles/", ArticleListCreateApi.as_view(), name = "article-list"),
    path("articles/<int:pk>", ArticleDetailView.as_view(), name = "article-detail"),
]
