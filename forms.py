from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(label='Ask somehting you want to know ', max_length=255)
