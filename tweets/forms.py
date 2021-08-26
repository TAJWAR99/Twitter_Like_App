from .models import Tweet
from django import forms

MAX_TWEET_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH or len(content)<1:
            raise forms.ValidationError("Length is too large or small")
        return content