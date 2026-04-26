from django.db import models
from customers.models import Customer
from django.core.validators import FileExtensionValidator, RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+996\d{8,9}$', message="Phone number must start with +996 and contain 8 or 9 digits.")


class Document(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name='documents')

    passport_customer = models.ImageField(
        upload_to='passports/customer/%Y/%m/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])
    passport_wife = models.ImageField(
        upload_to='passports/wife/%Y/%m/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])
    installment_contract = models.ImageField(
        upload_to='contracts/%Y/%m/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])
    car_tech_passport = models.ImageField(
        upload_to='tech_passports/%Y/%m/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])

    car_photo_front = models.ImageField(upload_to='car_photos/front/%Y/%m/', validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg', 'webp'])], blank=True, null=True, verbose_name="Car Photo (Front)")
    car_photo_back = models.ImageField(upload_to='car_photos/back/%Y/%m/', validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg', 'webp'])], blank=True, null=True, verbose_name="Car Photo (Back)")
    car_photo_left = models.ImageField(upload_to='car_photos/left/%Y/%m/', validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg', 'webp'])], blank=True, null=True, verbose_name="Car Photo (Left)")
    car_photo_right = models.ImageField(upload_to='car_photos/right/%Y/%m/', validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg', 'webp'])], blank=True, null=True, verbose_name="Car Photo (Right)")

    relative_1_phone = models.CharField(validators=[
                                        phone_regex], max_length=50, blank=True, null=True, verbose_name="Relative 1 Phone")
    relative_2_phone = models.CharField(validators=[
                                        phone_regex], max_length=50, blank=True, null=True, verbose_name="Relative 2 Phone")
    relative_3_phone = models.CharField(validators=[
                                        phone_regex], max_length=50, blank=True, null=True, verbose_name="Relative 3 Phone")
    relative_4_phone = models.CharField(validators=[
                                        phone_regex], max_length=50, blank=True, null=True, verbose_name="Relative 4 Phone")
    relative_5_phone = models.CharField(validators=[
                                        phone_regex], max_length=50, blank=True, null=True, verbose_name="Relative 5 Phone")

    def __str__(self):
        return f"Documents for {self.customer.full_name}"
