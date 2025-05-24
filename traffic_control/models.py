from django.db import models
from django.utils import timezone

class Intersection(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название перекрестка")
    location = models.CharField(max_length=200, verbose_name="Расположение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Перекресток"
        verbose_name_plural = "Перекрестки"

class TrafficLight(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активен'),
        ('inactive', 'Неактивен'),
        ('maintenance', 'На обслуживании'),
    ]
    
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE, verbose_name="Перекресток")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inactive', verbose_name="Статус")
    installation_date = models.DateField(verbose_name="Дата установки")
    last_maintenance = models.DateField(null=True, blank=True, verbose_name="Последнее обслуживание")
    
    def __str__(self):
        return f"Светофор {self.id} - {self.intersection.name}"
    
    class Meta:
        verbose_name = "Светофор"
        verbose_name_plural = "Светофоры"

class TrafficLightHistory(models.Model):
    traffic_light = models.ForeignKey(TrafficLight, on_delete=models.CASCADE, verbose_name="Светофор")
    turn_on_time = models.DateTimeField(verbose_name="Время включения")
    turn_off_time = models.DateTimeField(null=True, blank=True, verbose_name="Время выключения")
    cars_passed = models.IntegerField(default=0, verbose_name="Количество проехавших автомобилей")
    cars_waiting = models.IntegerField(default=0, verbose_name="Количество автомобилей в ожидании")
    
    def __str__(self):
        return f"История {self.traffic_light} - {self.turn_on_time.strftime('%d.%m.%Y %H:%M')}"
    
    def get_formatted_turn_on_time(self):
        return self.turn_on_time.strftime('%d.%m.%Y %H:%M')
    
    def get_formatted_turn_off_time(self):
        if self.turn_off_time:
            return self.turn_off_time.strftime('%d.%m.%Y %H:%M')
        return "-"
    
    class Meta:
        verbose_name = "История светофора"
        verbose_name_plural = "История светофоров"

class TrafficStatistics(models.Model):
    traffic_light = models.ForeignKey(TrafficLight, on_delete=models.CASCADE, verbose_name="Светофор")
    date = models.DateField(verbose_name="Дата")
    total_cars = models.IntegerField(default=0, verbose_name="Всего автомобилей")
    peak_hour = models.TimeField(verbose_name="Час пик")
    average_wait_time = models.IntegerField(verbose_name="Среднее время ожидания (сек)")
    
    def __str__(self):
        return f"Статистика {self.traffic_light} - {self.date}"
    
    def get_formatted_date(self):
        return self.date.strftime('%d.%m.%Y')
    
    class Meta:
        verbose_name = "Статистика движения"
        verbose_name_plural = "Статистика движения"

class MaintenanceRecord(models.Model):
    traffic_light = models.ForeignKey(TrafficLight, on_delete=models.CASCADE, verbose_name="Светофор")
    maintenance_date = models.DateField(verbose_name="Дата обслуживания")
    description = models.TextField(verbose_name="Описание работ")
    technician = models.CharField(max_length=100, verbose_name="Техник")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    
    def __str__(self):
        return f"Обслуживание {self.traffic_light} - {self.maintenance_date}"
    
    class Meta:
        verbose_name = "Запись об обслуживании"
        verbose_name_plural = "Записи об обслуживании"
