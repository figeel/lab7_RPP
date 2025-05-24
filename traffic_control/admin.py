from django.contrib import admin
from .models import Intersection, TrafficLight, TrafficLightHistory, TrafficStatistics, MaintenanceRecord

@admin.register(Intersection)
class IntersectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at')
    search_fields = ('name', 'location')

@admin.register(TrafficLight)
class TrafficLightAdmin(admin.ModelAdmin):
    list_display = ('id', 'intersection', 'status', 'installation_date', 'last_maintenance')
    list_filter = ('status', 'installation_date')
    search_fields = ('intersection__name',)

@admin.register(TrafficLightHistory)
class TrafficLightHistoryAdmin(admin.ModelAdmin):
    list_display = ('traffic_light', 'turn_on_time', 'turn_off_time', 'cars_passed', 'cars_waiting')
    list_filter = ('turn_on_time', 'turn_off_time')
    search_fields = ('traffic_light__intersection__name',)

@admin.register(TrafficStatistics)
class TrafficStatisticsAdmin(admin.ModelAdmin):
    list_display = ('traffic_light', 'date', 'total_cars', 'peak_hour', 'average_wait_time')
    list_filter = ('date',)
    search_fields = ('traffic_light__intersection__name',)

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('traffic_light', 'maintenance_date', 'technician', 'cost')
    list_filter = ('maintenance_date',)
    search_fields = ('traffic_light__intersection__name', 'technician')
