from rest_framework import viewsets, permissions
from .models import  Task
from .serializers import TaskSerializer

# conjunto de vistas donde cada vez que se crea una ruta se puede crear las funciones de CRUD
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() # consulta y extrae toda la información del modelo Task
    permission_classes = [permissions.AllowAny] # habilita permisos para pasar por rutas sin autenticacion
    serializer_class = TaskSerializer