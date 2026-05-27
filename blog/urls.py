from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create-post/', views.create_post, name='create_post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
]