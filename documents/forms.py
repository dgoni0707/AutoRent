from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'passport_customer', 'passport_wife', 'installment_contract', 'car_tech_passport',
            'car_photo_front', 'car_photo_back', 'car_photo_left', 'car_photo_right',
            'relative_1_phone', 'relative_2_phone', 'relative_3_phone', 'relative_4_phone', 'relative_5_phone'
        ]
        widgets = {
            'passport_customer': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'passport_wife': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'installment_contract': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'car_tech_passport': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'car_photo_front': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'car_photo_back': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'car_photo_left': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'car_photo_right': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'relative_1_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996...'}),
            'relative_2_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996...'}),
            'relative_3_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996...'}),
            'relative_4_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996...'}),
            'relative_5_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+996...'}),
        }
