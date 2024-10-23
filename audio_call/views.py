from django.shortcuts import render

def audio_call(request, room_name):
    return render(request, 'audio_call/audio_call.html', {
        'room_name': room_name
    })
