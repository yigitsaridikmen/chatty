from django.urls import path, include
from chatapp import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views as account_view

urlpatterns = [
	# path("storedchat/", chat_views.chatPage, name="storedchat"),
	path("instantchat/", chat_views.chatPage, name="instantchat/"),
	path("gptchat/", chat_views.message_list, name="gptchat"),
	path("handlechat/", chat_views.create_message, name="handlechat/"),
	# path("handlechat/", chat_views.message_list, name="handlechat/"),
	path("", chat_views.message_list, name="chat-page"),
	# login-section
	path("auth/login/", LoginView.as_view
		(template_name="chatapp/loginpage.html"), name="login-user"),
	path("auth/logout/", LogoutView.as_view(), name="logout-user"),
	path("accounts/signup/", account_view.SignUpView.as_view(), name="signup"),
]
