from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app_main.api.permissions import IsOwnerOrAdminUser
from app_main.models import Distrito, Presbiterio
from app_main.api.serializers import DistritoSerializer, PresbiterioSerializer, UserSerializer


# Create your views here.
class DistritoVS(viewsets.ReadOnlyModelViewSet):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer
    permission_classes = [IsAuthenticated]


class PresbiterioVS(viewsets.ModelViewSet):
    queryset = Presbiterio.objects.all()
    serializer_class = PresbiterioSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if bool(self.request.user.is_superstar):
                return queryset
            if (self.request.user.role == '2' or self.request.user.role == '2') and self.request.user.distrito:
                distrito = self.request.user.distrito
                users = distrito.user_set.all()
                return queryset.filter(user__in=users)
        return queryset.none()


userModel = get_user_model()


class UserVS(viewsets.ReadOnlyModelViewSet):
    queryset = userModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(is_superstar=True)
