from django import forms

class UseridForm(forms.Form):
    user_id = forms.CharField()