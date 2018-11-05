from django.urls import path
from .views import PostView, PostDetailView, PostCreateView, PostEditView, SignupView

app_name = 'blog'
urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='posts-detail'),
    path('create/', PostCreateView.as_view(), name='posts-create'),
    path('edit/<int:id>/', PostEditView.as_view(), name='posts-edit'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
]
