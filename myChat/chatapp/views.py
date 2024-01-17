from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import MessageForm  # Import your form if you have one
from django.views.decorators.csrf import csrf_exempt
import json

# Chatgpt api
from django.http import JsonResponse
from .gptapi import gptBot
from .consumers import ChatConsumer
import asyncio
from django.urls import reverse
# Create your views here.
def chatPage(request, *args, **kwargs):
    
	if not request.user.is_authenticated:
		return redirect("login-user")
    
	context = {}

	return render(request, "chatapp/chatpage.html", context)

@csrf_exempt  # Ensure proper CSRF protection in production
def create_message(request):
    
    if request.method == 'POST':
        myrequest = json.loads(request.body)
        message_text = myrequest['message_text']
        username = myrequest['username']
        form = MessageForm(myrequest)  
        if form.is_valid() and request.user.username==username:
            username = form.cleaned_data['username']
            message_text = form.cleaned_data['message_text']
            Message.objects.create(username=username, message_text=message_text, created_at=timezone.now() + timezone.timedelta(hours=3))
            if message_text[:4]=='@gpt':
                response = gptBot(username,message_text[5:])
                Message.objects.create(username='GPT', message_text=response, created_at=timezone.now() + timezone.timedelta(hours=3))
                
                return JsonResponse({'message':response})
    else:
        form = MessageForm()


    return render(request, 'chatapp/chatpage.html', {'form': form})

@login_required(login_url='auth/login/')
def message_list(request):
    qs = Message.objects.all()
    value_today = timezone.now().date()
    context={
        "object_list":qs,
        'value_today': value_today,
    }
    
    return render(request, "chatapp/chatpage.html", context=context)




