from django.db.models import Sum
from django.db.models.functions import TruncMonth
from collections import defaultdict
from .models import Payment

class PaymentService:
    @staticmethod
    def get_total_paid_for_customer(customer):
        total = Payment.objects.filter(customer=customer).aggregate(total=Sum('amount'))['total']
        return total or 0

    @staticmethod
    def get_monthly_totals_for_customer(customer):
        totals = (Payment.objects.filter(customer=customer)
                  .annotate(month=TruncMonth('date'))
                  .values('month')
                  .annotate(total=Sum('amount'))
                  .order_by('-month'))
        return list(totals)

    @staticmethod
    def get_payments_grouped_by_month(customer):
        payments = Payment.objects.filter(customer=customer).order_by('-date', '-time')
        grouped = defaultdict(list)
        for payment in payments:
            month_key = payment.date.strftime("%B %Y")
            grouped[month_key].append(payment)
        return dict(grouped)
