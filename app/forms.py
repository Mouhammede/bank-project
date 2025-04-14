from django import forms
from .views import user
class userregisterform(forms.Form):
    ssn=forms.IntegerField()
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)

