from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from tasks.views import UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('auth/register/', UserRegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Tasks CRUD
    path('', include('tasks.urls')),

    # API Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger & ReDoc
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

