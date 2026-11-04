
from django.db import models


class Device(models.Model):

    VENDOR_CHOICES = [
        ('Huawei', 'Huawei'),
        ('ZTE', 'ZTE'),
        ('FiberHome', 'FiberHome'),
    ]

    STATUS_CHOICES = [
        ('Ready', 'Ready'),
        ('In Use', 'In Use'),
        ('Offline', 'Offline'),
    ]

    vendor = models.CharField(
        max_length=50,
        choices=VENDOR_CHOICES
    )

    model = models.CharField(max_length=100)

    firmware = models.CharField(
        max_length=100,
        blank=True
    )

    ip_address = models.GenericIPAddressField(
        protocol='IPv4'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Ready'
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vendor} {self.model} - {self.ip_address}"
