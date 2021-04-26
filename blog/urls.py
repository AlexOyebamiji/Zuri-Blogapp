from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateview, BlogUpdateView, BlogDeleteView, BlogSignUpView, LoginView, LogoutView, CommentCreateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'), 
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='post-detail'),
    path('post/new/', BlogCreateview.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', BlogSignUpView.as_view(), name='signup'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetView.as_view(), name='password_reset_complete'),
    path('', BlogListView.as_view(), name='home'),
]