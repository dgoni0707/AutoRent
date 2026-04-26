from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:customer_id>/',
         views.upload_documents, name='upload_documents'),
]
