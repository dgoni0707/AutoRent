from .models import Document

class DocumentService:
    @staticmethod
    def get_documents_for_customer(customer):
        try:
            return customer.documents
        except Document.DoesNotExist:
            return None
