from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Friend, Profile

# Landing page with links to register and login
def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect authenticated users to home
    return render(request, 'accounts/landing.html')

# Home page after login
@login_required
def home(request):
    return render(request, 'accounts/home.html')

# Registration view
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if not username or not password:
            return HttpResponse("Username and password are required.")

        if password != password_confirm:
            return HttpResponse("Passwords do not match.")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken.")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login credentials.")

    return render(request, 'accounts/login.html')

# Logout view
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing_page')

# Profile view
@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': user_profile})

# Edit profile view
@login_required
def edit_profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        picture = request.FILES.get('picture')

        user_profile.bio = bio
        if picture:
            user_profile.picture = picture
        user_profile.save()

        return redirect('profile')

    return render(request, 'accounts/edit_profile.html', {'profile': user_profile})

# Send friend request
@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)

    if request.user == to_user:
        return HttpResponse("You cannot send a friend request to yourself.")

    if Friend.objects.filter(from_user=request.user, to_user=to_user).exists():
        return HttpResponse("Friend request already sent.")

    Friend.objects.create(from_user=request.user, to_user=to_user)
    return redirect('friend_list')

# Accept friend request
@login_required
def accept_friend_request(request, friend_id):
    friend_request = get_object_or_404(Friend, id=friend_id, to_user=request.user)

    if friend_request.is_accepted:
        return HttpResponse("Friend request already accepted.")

    friend_request.is_accepted = True
    friend_request.save()
    return redirect('friend_list')

# Decline friend request
@login_required
def decline_friend_request(request, friend_id):
    friend_request = get_object_or_404(Friend, id=friend_id, to_user=request.user)
    friend_request.delete()
    return redirect('friend_requests')

# Friend list view
@login_required
def friend_list(request):
    friends_from_user = Friend.objects.filter(is_accepted=True, from_user=request.user)
    friends_to_user = Friend.objects.filter(is_accepted=True, to_user=request.user)
    
    # Combine both queries into a single list
    friends = friends_from_user | friends_to_user
    
    return render(request, 'accounts/friend_list.html', {'friends': friends})

# View all users to send friend requests
@login_required
def all_users(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'accounts/all_users.html', {'users': users})

# View friend requests sent to the user
@login_required
def friend_requests(request):
    received_requests = Friend.objects.filter(to_user=request.user, is_accepted=False)
    return render(request, 'accounts/friend_requests.html', {'friend_requests': received_requests})
