
from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm


def dashboard(request):
    context = {
        'total_modem': Device.objects.count(),
        'qc_berhasil': 0,
        'qc_gagal': 0,
        'qc_proses': 0,
    }

    return render(request, 'qc_modem/dashboard.html', context)


def device_list(request):
    devices = Device.objects.all().order_by('-created_at')

    return render(request, 'qc_modem/device_list.html', {
        'devices': devices
    })


def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()

    return render(request, 'qc_modem/device_form.html', {
        'form': form,
        'title': 'Tambah Perangkat'
    })


def device_update(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)

        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm(instance=device)

    return render(request, 'qc_modem/device_form.html', {
        'form': form,
        'title': 'Edit Perangkat'
    })


def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if request.method == 'POST':
        device.delete()
        return redirect('device_list')

    return render(request, 'qc_modem/device_confirm_delete.html', {
        'device': device
    })
