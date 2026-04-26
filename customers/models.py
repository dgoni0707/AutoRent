from django.db import models
from django.urls import reverse

class Customer(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Full Name (FIO)")
    license_plate = models.CharField(max_length=20, verbose_name="Car license plate number")
    contract_date = models.DateField(verbose_name="Date of contract creation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.license_plate})"

    def get_absolute_url(self):
        return reverse('customer_profile', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
