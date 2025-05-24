from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import (
    TrafficLightHistory, TrafficLight, TrafficStatistics, 
    MaintenanceRecord, Intersection
)
from django.contrib.auth.models import Group

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'traffic_control/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'traffic_control/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object # Получаем созданного пользователя
        worker_group, created = Group.objects.get_or_create(name='Работник')
        user.groups.add(worker_group)
        return response

# Intersection views
class IntersectionListView(LoginRequiredMixin, ListView):
    model = Intersection
    template_name = 'traffic_control/intersection_list.html'
    context_object_name = 'intersections'
    login_url = 'login'

class IntersectionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Intersection
    template_name = 'traffic_control/intersection_form.html'
    fields = ['name', 'location']
    success_url = reverse_lazy('intersection-list')
    permission_required = 'traffic_control.add_intersection'
    login_url = 'login'

class IntersectionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Intersection
    template_name = 'traffic_control/intersection_form.html'
    fields = ['name', 'location']
    success_url = reverse_lazy('intersection-list')
    permission_required = 'traffic_control.change_intersection'
    login_url = 'login'

class IntersectionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Intersection
    template_name = 'traffic_control/intersection_confirm_delete.html'
    success_url = reverse_lazy('intersection-list')
    permission_required = 'traffic_control.delete_intersection'
    login_url = 'login'

# TrafficLight views
class TrafficLightListView(LoginRequiredMixin, ListView):
    model = TrafficLight
    template_name = 'traffic_control/trafficlight_list.html'
    context_object_name = 'traffic_lights'
    login_url = 'login'

class TrafficLightCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TrafficLight
    template_name = 'traffic_control/trafficlight_form.html'
    fields = ['intersection', 'status', 'installation_date', 'last_maintenance']
    success_url = reverse_lazy('trafficlight-list')
    permission_required = 'traffic_control.add_trafficlight'
    login_url = 'login'

class TrafficLightUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TrafficLight
    template_name = 'traffic_control/trafficlight_form.html'
    fields = ['intersection', 'status', 'installation_date', 'last_maintenance']
    success_url = reverse_lazy('trafficlight-list')
    permission_required = 'traffic_control.change_trafficlight'
    login_url = 'login'

class TrafficLightDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TrafficLight
    template_name = 'traffic_control/trafficlight_confirm_delete.html'
    success_url = reverse_lazy('trafficlight-list')
    permission_required = 'traffic_control.delete_trafficlight'
    login_url = 'login'

# TrafficLightHistory views
class TrafficLightHistoryListView(LoginRequiredMixin, ListView):
    model = TrafficLightHistory
    template_name = 'traffic_control/history_list.html'
    context_object_name = 'history_records'
    login_url = 'login'

class TrafficLightHistoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TrafficLightHistory
    template_name = 'traffic_control/history_form.html'
    fields = ['traffic_light', 'turn_on_time', 'turn_off_time', 'cars_passed', 'cars_waiting']
    success_url = reverse_lazy('history-list')
    permission_required = 'traffic_control.add_trafficlighthistory'
    login_url = 'login'

class TrafficLightHistoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TrafficLightHistory
    template_name = 'traffic_control/history_form.html'
    fields = ['traffic_light', 'turn_on_time', 'turn_off_time', 'cars_passed', 'cars_waiting']
    success_url = reverse_lazy('history-list')
    permission_required = 'traffic_control.change_trafficlighthistory'
    login_url = 'login'

class TrafficLightHistoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TrafficLightHistory
    template_name = 'traffic_control/history_confirm_delete.html'
    success_url = reverse_lazy('history-list')
    permission_required = 'traffic_control.delete_trafficlighthistory'
    login_url = 'login'

# Statistics views
class StatisticsListView(LoginRequiredMixin, ListView):
    model = TrafficStatistics
    template_name = 'traffic_control/statistics_list.html'
    context_object_name = 'statistics'
    login_url = 'login'

class StatisticsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TrafficStatistics
    template_name = 'traffic_control/statistics_form.html'
    fields = ['traffic_light', 'date', 'total_cars', 'peak_hour', 'average_wait_time']
    success_url = reverse_lazy('statistics-list')
    permission_required = 'traffic_control.add_trafficstatistics'
    login_url = 'login'

class StatisticsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TrafficStatistics
    template_name = 'traffic_control/statistics_form.html'
    fields = ['traffic_light', 'date', 'total_cars', 'peak_hour', 'average_wait_time']
    success_url = reverse_lazy('statistics-list')
    permission_required = 'traffic_control.change_trafficstatistics'
    login_url = 'login'

class StatisticsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TrafficStatistics
    template_name = 'traffic_control/statistics_confirm_delete.html'
    success_url = reverse_lazy('statistics-list')
    permission_required = 'traffic_control.delete_trafficstatistics'
    login_url = 'login'

# Maintenance views
class MaintenanceListView(LoginRequiredMixin, ListView):
    model = MaintenanceRecord
    template_name = 'traffic_control/maintenance_list.html'
    context_object_name = 'maintenance_records'
    login_url = 'login'

class MaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = MaintenanceRecord
    template_name = 'traffic_control/maintenance_form.html'
    fields = ['traffic_light', 'maintenance_date', 'description', 'technician', 'cost']
    success_url = reverse_lazy('maintenance-list')
    permission_required = 'traffic_control.add_maintenancerecord'
    login_url = 'login'

class MaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MaintenanceRecord
    template_name = 'traffic_control/maintenance_form.html'
    fields = ['traffic_light', 'maintenance_date', 'description', 'technician', 'cost']
    success_url = reverse_lazy('maintenance-list')
    permission_required = 'traffic_control.change_maintenancerecord'
    login_url = 'login'

class MaintenanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MaintenanceRecord
    template_name = 'traffic_control/maintenance_confirm_delete.html'
    success_url = reverse_lazy('maintenance-list')
    permission_required = 'traffic_control.delete_maintenancerecord'
    login_url = 'login'
