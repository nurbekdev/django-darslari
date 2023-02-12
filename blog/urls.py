from django.urls import path
from .views import (HomePageView,
                    BlogDetailView,
                    CreatePageView,
                    EditPostView,
                    DeletePostView)

urlpatterns = [
    path("",HomePageView.as_view(),name='home'),
    path("post/<int:pk>/",BlogDetailView.as_view(),name='detail'),
    path("post/new",CreatePageView.as_view(),name='post_new'),
    path("post/<int:pk>/edit",EditPostView.as_view(),name='post_edit'),
    path("post/<int:pk>/delete",DeletePostView.as_view(),name='delete'),

]