from rest_framework import serializers

from app_main.models import Distrito, Presbiterio


class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = '__all__'
        read_only_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'bautizados_espiritu',
                           'promedio_asistencia', 'cant_presbiterios', 'total_departamento')


class PresbiterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presbiterio
        exclude = ['user']
        read_only_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'bautizados_espiritu',
                           'promedio_asistencia', 'total_departamento')
        depth = 1
