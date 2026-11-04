
from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = [
            'vendor',
            'model',
            'firmware',
            'ip_address',
            'status',
            'notes',
        ]

        widgets = {
            'vendor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: HG8245H'
            }),
            'firmware': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Versi firmware'
            }),
            'ip_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: 192.168.1.1'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
