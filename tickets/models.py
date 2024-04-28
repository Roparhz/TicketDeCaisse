from django.db import models

class Ticket (models.Model):
    date = models.DateField(unique=True)
    intitule = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ticket {self.id}: {self.intitule}: ({self.date})"
