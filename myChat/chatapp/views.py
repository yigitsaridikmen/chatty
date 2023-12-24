from django.shortcuts import render, redirect
from .models import Message
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import MessageForm  # Import your form if you have one
from django.views.decorators.csrf import csrf_exempt
import json

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
    print('View triggered')
    print('My request method: ',request.method)
    if request.method == 'POST' or request.method is None:
        print('Request is post or none!')
        #print(request.POST)
        print('test')
        print(json.load(request.body))
		#received_data = json.loads(request.body)
        #print(received_data)
        form = MessageForm(request.POST)  # Assuming you have a form for creating messages
        print(form,form.is_valid)
        if form.is_valid():
            print('form is valid')
            username = form.cleaned_data['username']
            message_text = form.cleaned_data['message_text']
            form.save()
            print('form saved')
            Message.objects.create(username=username, message_text=message_text, created_at=timezone.now())
            print('Post received create message worked')
            
            #return HttpResponseRedirect('/')  # Redirect to the message list after creating the message
    else:
        print('else')
        form = MessageForm()  # Assuming you have a form for creating messages
	
	
    return render(request, 'chatapp/chatpage.html', {'form': form})



