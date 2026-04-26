from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customers.models import Customer
from .forms import DocumentForm
from .models import Document


@login_required
def upload_documents(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    # Check if documents already exist for this customer
    try:
        instance = customer.documents
    except Document.DoesNotExist:
        instance = None

    # Check permissions: managers cannot change existing documents
    if instance and not request.user.is_superuser:
        messages.error(
            request, "Managers cannot modify existing documents. Please contact an administrator.")
        return redirect('customer_profile', pk=customer.pk)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.customer = customer
            doc.save()
            messages.success(request, "Documents uploaded successfully.")
            return redirect('customer_profile', pk=customer.pk)
    else:
        form = DocumentForm(instance=instance)

    return render(request, 'documents/upload.html', {
        'form': form,
        'customer': customer,
        'is_edit': instance is not None
    })
