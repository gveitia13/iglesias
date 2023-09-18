from django.urls import path

from app_main.views import generar_reporte

urlpatterns = [
    path('generar_reporte/', generar_reporte, name='generar_reporte')
]
