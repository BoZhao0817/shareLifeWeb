from django import forms
# from django.forms import ModelForm
from .models import Post
class SubmitPostForm0(forms.Form):
    name = forms.CharField(help_text="Name your place", required= True)
    body = forms.CharField(help_text="Some introductions", required=False)
    location = forms.CharField(help_text= "your place", required= True)
    # location = forms.CharField(help_text="your place", required=True)

class SubmitPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name','location', 'body','address','startDate','endDate']
        labels = {'name': 'Name Your House', 'body':'some introduction'}



