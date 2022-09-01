from django import forms


class NewChatForm(forms.Form):
    room_name = forms.CharField(max_length=50)
