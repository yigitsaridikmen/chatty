from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["username","message_text","created_at"]
    def clean(self):
        print('Form is triggered')
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        message_text = cleaned_data.get("message_text")
        print(cleaned_data)
        return cleaned_data