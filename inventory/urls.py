from django.urls import path

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='index'),
    path('create_device', views.DeviceCreateView.as_view(), name='create_device'),
    path('<int:pk>/', views.DeviceDetailView.as_view(), name='device'),
    path('<int:pk>/edit_device', views.DeviceEditView.as_view(), name='edit_device'),
    path('<int:pk>/delete_device', views.DeviceDeleteView.as_view(), name='delete_device'),
]
