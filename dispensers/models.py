from django.db import models

class Dispenser(models.Model):

    flow_volume = models.DecimalField(max_digits=10, decimal_places=5)  # In liters per second
    is_open = models.BooleanField(default=False)
    opened_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    total_money = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"Dispenser {self.id}"
