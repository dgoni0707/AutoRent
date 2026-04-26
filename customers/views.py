from datetime import date, timedelta
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from payments.services import PaymentService
from documents.services import DocumentService


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 20


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customer_profile.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.object
        context['documents'] = DocumentService.get_documents_for_customer(
            customer)
        context['total_paid'] = PaymentService.get_total_paid_for_customer(
            customer)
        context['monthly_totals'] = PaymentService.get_monthly_totals_for_customer(
            customer)
        context['payments_by_month'] = PaymentService.get_payments_grouped_by_month(
            customer)
        return context


class CustomerCalendarView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/payment_calendar.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.object

        if not customer.contract_date:
            return context

        today = date.today()
        start_date = customer.contract_date

        # We'll show days from contract_date up to the end of the current month
        # or maybe just up to today if that's what the user meant.
        # "если один день без оплаты остается до сегоднешнего дня то он просрочен"
        # Let's show up to today + some buffer or just up to today.
        # Actually, showing at least the current month is better for a "calendar".

        # Calculate end_date: end of current month
        if today.month == 12:
            next_month = date(today.year + 1, 1, 1)
        else:
            next_month = date(today.year, today.month + 1, 1)
        end_date = next_month - timedelta(days=1)

        payments_dates = set(customer.payments.values_list('date', flat=True))

        months_data = []
        curr = start_date
        current_month_days = []
        current_month_label = curr.strftime('%B %Y')

        while curr <= end_date:
            is_paid = curr in payments_dates

            if is_paid:
                status = 'paid'
            elif curr < today:
                status = 'overdue'
            else:
                status = 'pending'

            # If month changes, push current month to months_data
            month_label = curr.strftime('%B %Y')
            if month_label != current_month_label:
                months_data.append({
                    'label': current_month_label,
                    'days': current_month_days
                })
                current_month_days = []
                current_month_label = month_label

            current_month_days.append({
                'date': curr,
                'status': status
            })
            curr += timedelta(days=1)

        # Final month
        if current_month_days:
            months_data.append({
                'label': current_month_label,
                'days': current_month_days
            })

        context['months'] = months_data
        return context
