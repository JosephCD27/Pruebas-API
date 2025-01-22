from rest_framework import serializers #importa el serializador
from .models import Task #importa el modelo Task

# esto se va a usar al momento de hacer llamadas en rutas
class TaskSerializer(serializers.ModelSerializer): # a las clase sele importa ModelSerializer
    class Meta:
        model = Task
        fields = ("id","titulo","descripcion","hecho","creacion")
        read_only_fields = ("id","creacion")
