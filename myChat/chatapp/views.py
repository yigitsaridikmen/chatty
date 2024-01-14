from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import MessageForm  # Import your form if you have one
from django.views.decorators.csrf import csrf_exempt
import json

# Chatgpt api
from django.http import HttpResponse
from .gptapi import gptBot
from .consumers import ChatConsumer
# Create your views here.
def chatPage(request, *args, **kwargs):
    
	if not request.user.is_authenticated:
		return redirect("login-user")
     
	context = {}

	return render(request, "chatapp/chatpage.html", context)

# def message_list(request):
#     messages = Message.objects.all().order_by('-created_at')  # Fetch all messages ordered by creation datetime
#     return render(request, 'message_list.html', {'messages': messages})
@csrf_exempt  # Ensure proper CSRF protection in production
def create_message(request):
    if request.method == 'POST':
        myrequest = json.loads(request.body)
        message_text = myrequest['message_text']
        username = myrequest['username']
        form = MessageForm(myrequest)  
        is_gptActive = False
        if form.is_valid() and request.user.username==username:
            print('form is valid')
            username = form.cleaned_data['username']
            message_text = form.cleaned_data['message_text']
            Message.objects.create(username=username, message_text=message_text, created_at=timezone.now() + timezone.timedelta(hours=3))
            print('Post received create message worked')
            if message_text[:4]=='@gpt':
                response = gptBot(username,message_text[5:])
                print('GPTS RESPONSE',response)
                Message.objects.create(username='GPT', message_text=response, created_at=timezone.now() + timezone.timedelta(hours=3))
                async_send_json = {
                     "message":response,"username":'GPT'
                }
                is_gptActive = True
                # Refresh when is_gptActive is True
                # return  redirect('../gptchat/')
                # ASYNC JSON {"message":"@gpt where is Manisa?\n","username":"yigidos"}
    else:
        print('else')
        form = MessageForm()


    return render(request, 'chatapp/chatpage.html', {'form': form})

@login_required(login_url='auth/login/')
def message_list(request):
    print('view triggered')
    qs = Message.objects.all()
    value_today = timezone.now().date()
    context={
        "object_list":qs,
        'value_today': value_today
    }
    
    return render(request, "chatapp/chatpage.html", context=context)


