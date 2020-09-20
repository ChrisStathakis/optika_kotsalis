from django.urls import path

from .views import PostListView, PostDetailView

urlpatterns = [
    path('list/', PostListView.as_view(), name='post_list'),
    path('detail/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
   ]