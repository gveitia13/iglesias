from django.urls import path

from app_main.views import generar_reporte, print_reporte

urlpatterns = [
    path('generar_reporte/', generar_reporte, name='generar_reporte'),
    path('print_reporte/<int:pk>/', print_reporte, name='print_reporte'),
]
