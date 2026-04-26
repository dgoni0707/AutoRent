from django.db import models
from customers.models import Customer

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField(blank=True, null=True, verbose_name="Optional check/comment")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.amount} by {self.customer.full_name} on {self.date}"
