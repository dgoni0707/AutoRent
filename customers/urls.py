from django.urls import path
from .views import CustomerListView, CustomerDetailView, CustomerCalendarView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(),
         name='customer_profile'),
    path('customer/<int:pk>/calendar/',
         CustomerCalendarView.as_view(), name='customer_calendar'),
]
