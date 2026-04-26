from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from .services import PaymentService
from customers.models import Customer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def customer_totals(self, request):
        customer_id = request.query_params.get('customer_id')
        if not customer_id:
            return Response({'error': 'customer_id is required'}, status=400)
            
        try:
            customer = Customer.objects.get(pk=customer_id)
            total = PaymentService.get_total_paid_for_customer(customer)
            monthly = PaymentService.get_monthly_totals_for_customer(customer)
            return Response({
                'total_paid': total,
                'monthly_totals': monthly
            })
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=404)
