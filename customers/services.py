from .models import Customer
from documents.models import Document

class CustomerService:
    @staticmethod
    def get_all_customers():
        return Customer.objects.all()

    @staticmethod
    def get_customer_profile(customer_id):
        return Customer.objects.prefetch_related('documents', 'payments').get(pk=customer_id)
