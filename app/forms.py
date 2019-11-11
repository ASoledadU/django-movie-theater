from django import forms


class NewTicketForm(forms.Form):
    name = forms.TextField()
    showing_id = forms.IntegerField()
