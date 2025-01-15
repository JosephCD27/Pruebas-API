from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Crea una instancia del router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# Agrega las rutas
urlpatterns = [
    path('api/v1/', include(router.urls)),
]