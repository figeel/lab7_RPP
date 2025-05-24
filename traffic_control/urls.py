from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('', views.TrafficLightHistoryListView.as_view(), name='history-list'),
    path('history/create/', views.TrafficLightHistoryCreateView.as_view(), name='history-create'),
    path('history/<int:pk>/update/', views.TrafficLightHistoryUpdateView.as_view(), name='history-update'),
    path('history/<int:pk>/delete/', views.TrafficLightHistoryDeleteView.as_view(), name='history-delete'),
    
    path('statistics/', views.StatisticsListView.as_view(), name='statistics-list'),
    path('statistics/create/', views.StatisticsCreateView.as_view(), name='statistics-create'),
    path('statistics/<int:pk>/update/', views.StatisticsUpdateView.as_view(), name='statistics-update'),
    path('statistics/<int:pk>/delete/', views.StatisticsDeleteView.as_view(), name='statistics-delete'),
    
    path('maintenance/', views.MaintenanceListView.as_view(), name='maintenance-list'),
    path('maintenance/create/', views.MaintenanceCreateView.as_view(), name='maintenance-create'),
    path('maintenance/<int:pk>/update/', views.MaintenanceUpdateView.as_view(), name='maintenance-update'),
    path('maintenance/<int:pk>/delete/', views.MaintenanceDeleteView.as_view(), name='maintenance-delete'),
    
    path('intersections/', views.IntersectionListView.as_view(), name='intersection-list'),
    path('intersections/create/', views.IntersectionCreateView.as_view(), name='intersection-create'),
    path('intersections/<int:pk>/update/', views.IntersectionUpdateView.as_view(), name='intersection-update'),
    path('intersections/<int:pk>/delete/', views.IntersectionDeleteView.as_view(), name='intersection-delete'),

    path('trafficlights/', views.TrafficLightListView.as_view(), name='trafficlight-list'),
    path('trafficlights/create/', views.TrafficLightCreateView.as_view(), name='trafficlight-create'),
    path('trafficlights/<int:pk>/update/', views.TrafficLightUpdateView.as_view(), name='trafficlight-update'),
    path('trafficlights/<int:pk>/delete/', views.TrafficLightDeleteView.as_view(), name='trafficlight-delete'),

    path('accounts/register/', RegisterView.as_view(), name='register'),
] 