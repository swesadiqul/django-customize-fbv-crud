from django import forms


#create forms here
class FeedbackForm(forms.Form):
    name = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()