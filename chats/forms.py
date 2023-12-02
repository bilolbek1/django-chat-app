from django.forms import ModelForm

from chats.models import Messages


class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['text']