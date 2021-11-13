from django import forms


class FutureContentRequest(forms.Form):
    content_request = forms.Textarea(help_text="What games/decks would you like to see in the future?")
