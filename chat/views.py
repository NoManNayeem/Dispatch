from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Chat, Message

@login_required
def chat_with_user(request, user_id):
    """
    View to initiate or retrieve a chat between two users and display the chat history.
    """
    other_user = get_object_or_404(User, id=user_id)
    
    # Check if a chat exists between these two users
    chat = Chat.objects.filter(participants=request.user).filter(participants=other_user).first()
    
    if not chat:
        # If no chat exists, create a new one
        chat = Chat.objects.create()
        chat.participants.add(request.user, other_user)
    
    # Fetch the chat messages, ordered by timestamp
    messages = chat.messages.order_by('timestamp')
    
    return render(request, 'chat/chat_room.html', {
        'chat': chat,
        'messages': messages,
        'other_user': other_user,
    })

@login_required
def send_message(request, chat_id):
    """
    View to send a message to the chat.
    """
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        message_content = request.POST.get('message')

        if message_content:
            # Create and save the new message
            Message.objects.create(
                chat=chat,
                sender=request.user,
                content=message_content
            )

    # Redirect back to the chat view
    other_user = chat.participants.exclude(id=request.user.id).first()
    return redirect('chat_with_user', user_id=other_user.id)

@login_required
def chat_list(request):
    """
    View to show a list of all chats the current user is involved in.
    """
    chats = Chat.objects.filter(participants=request.user)
    
    return render(request, 'chat/chat_list.html', {
        'chats': chats,
    })
