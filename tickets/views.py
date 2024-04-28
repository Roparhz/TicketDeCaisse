from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Ticket
from .forms import TicketForm
from django.urls import reverse_lazy

class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list.html'

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket-list')

class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ['date', 'intitule', 'montant']
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket-list')

class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket-list')
    template_name = 'ticket_delete.html'
