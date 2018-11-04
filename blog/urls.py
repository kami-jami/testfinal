from django.urls import path
from .views import PostView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='posts-detail'),
]
