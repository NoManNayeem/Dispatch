from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page (login/register links)
    path('home/', views.home, name='home'),  # Home page (requires login)
    path('register/', views.register, name='register'),  # Custom registration
    path('login/', views.login_view, name='login'),  # Custom login
    path('logout/', views.logout_view, name='logout'),  # Logout (POST request)
    path('profile/', views.profile, name='profile'),  # User profile view
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Edit profile view
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),  # Send friend request
    path('accept_friend_request/<int:friend_id>/', views.accept_friend_request, name='accept_friend_request'),  # Accept friend request
    path('decline_friend_request/<int:friend_id>/', views.decline_friend_request, name='decline_friend_request'),
    path('friends/', views.friend_list, name='friend_list'),  # List of friends
    path('users/', views.all_users, name='all_users'),  # View all users to send friend requests
    path('friend_requests/', views.friend_requests, name='friend_requests'),  # View incoming friend requests
]
