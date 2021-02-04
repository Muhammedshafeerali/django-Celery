from django import forms
from .tasks import send_review_email_task

class ReviewForm(forms.Form):
    name=forms.CharField(label='Firstnaem',min_length=4,widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    email1 = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    email2 = forms.EmailField(
        max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    email3 = forms.EmailField(
        max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    review = forms.CharField(
        label="Review", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))


    
    def send_email(self):
        email_list=[]
        email_list.extend([self.cleaned_data['email1'],self.cleaned_data['email2'],self.cleaned_data['email3']])
        send_review_email_task.delay(
            self.cleaned_data['name'], email_list, self.cleaned_data['review'])
