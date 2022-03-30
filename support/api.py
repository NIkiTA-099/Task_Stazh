from .models import Support, Answer
from rest_framework import viewsets, permissions
from .serializers import SupportSerializer, AnswerSerializer

class SupportViewSet(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = SupportSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnswerSerializer