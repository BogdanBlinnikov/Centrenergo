from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, DeleteView
from django_filters.views import FilterView

# from inventory.filters import DeviceFilter
from inventory.filters import DeviceCharsFilter
from inventory.models import Device, DeviceChars
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


class DeviceListView(PermissionRequiredMixin, FilterView):
    template_name = 'inventory/index.html'
    # context_object_name = 'devices'
    permission_required = 'inventory.index'
    filterset_class = DeviceCharsFilter

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(DeviceListView, self).get_context_data(**kwargs)
    #     print(context['filter'].__dict__)
    #     return context
    # def get_queryset(self):
    #     return Device.objects.all().order_by('inv_num')

    def handle_no_permission(self):
        return super().handle_no_permission()


class DeviceCharsCreateInLine(InlineFormSetFactory):
    model = DeviceChars
    fields = ['brand_name', 'model_name', 'diagonal', 'motherboard', 'processor',
              'clock_frequency', 'ram_type', 'ram_size', 'disk_space', 'windows']
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': False, }


class DeviceCreateView(PermissionRequiredMixin, CreateWithInlinesView):
    model = Device
    inlines = [DeviceCharsCreateInLine]
    template_name = 'inventory/create_device.html'
    fields = ['inv_num', 'user', 'type']
    permission_required = 'inventory.create_device'

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_success_url(self):
        return reverse('inventory:device', args=[self.object.id, ])


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'inventory/device.html'
    context_object_name = 'device'

    def get_context_data(self, **kwargs):
        device = super().get_context_data(**kwargs)
        devices = DeviceChars.objects.get(inv_num=self.object.id)
        device['device_chars'] = devices
        print(device)
        return device


class DeviceCharsEditInLine(InlineFormSetFactory):
    model = DeviceChars
    fields = ['brand_name', 'model_name', 'diagonal', 'motherboard', 'processor',
              'clock_frequency', 'ram_type', 'ram_size', 'disk_space', 'windows']
    factory_kwargs = {'extra': 0, 'max_num': None,
                      'can_order': False, 'can_delete': False}


class DeviceEditView(PermissionRequiredMixin, UpdateWithInlinesView):
    model = Device
    fields = ['inv_num', 'type', 'user']
    inlines = [DeviceCharsEditInLine]
    template_name = 'inventory/edit_device.html'
    permission_required = 'inventory:edit_device'

    def get_success_url(self):
        return reverse('inventory:device', args=[self.object.id, ])

    def handle_no_permission(self):
        return super().handle_no_permission()


class DeviceDeleteView(PermissionRequiredMixin, DeleteView):
    model = Device
    template_name = 'inventory/delete_device.html'
    permission_required = 'inventory.delete_device'

    def get_success_url(self):
        return reverse('inventory:index')

    def handle_no_permission(self):
        return super().handle_no_permission()
