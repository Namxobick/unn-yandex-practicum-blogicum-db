"""URLs of blog app."""
from django.urls import path
from .views import post_detail, CategoryListView, IndexView

app_name = 'blog'

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index'
    ),
    path(
        'posts/<int:post_id>/',
        post_detail,
        name='post_detail'
    ),
    path(
        'category/<slug:category_slug>/',
        CategoryListView.as_view(),
        name='category_posts'
    ),
]
