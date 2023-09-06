from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app_main.api.views import DistritoVS, PresbiterioVS, UserVS, get_distrito

router = DefaultRouter()
router.register('distrito', DistritoVS)
router.register('presbiterio', PresbiterioVS)
router.register('user', UserVS)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('get_distrito/', get_distrito, name='get_distrito')
]
