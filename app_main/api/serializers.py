from crum import get_current_user
from rest_framework import serializers

from app_main.models import Distrito, Presbiterio
from app_user.models import User
from iglesias import settings


class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = '__all__'
        read_only_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial', 'bautizados_espiritu',
                            'promedio_asistencia', 'cant_presbiterios', 'total_departamento')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name', ]
        depth = 1


class PresbiterioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, allow_null=True, required=False)
    distrito = serializers.SerializerMethodField()

    def get_distrito(self, object):
        if object.user:
            return object.user.distrito.__str__()
        user = get_current_user()
        return user.distrito.__str__()

    class Meta:
        model = Presbiterio
        # exclude = ['user']
        fields = '__all__'
        read_only_fields = ('fecha', 'total_cuerpo_ministerial', 'total_afiliacion_oficial',
                            'total_departamento', 'user')
        # depth = 1
