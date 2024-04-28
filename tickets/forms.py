from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['date', 'intitule', 'montant']

    def clean_date(self):
        date = self.cleaned_data.get("date")
        if Ticket.objects.filter(date=date).exists():
            raise forms.ValidationError("Un ticket avec cette date existe déjà.")
        return date
