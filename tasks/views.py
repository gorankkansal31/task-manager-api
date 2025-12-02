from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializer, UserRegisterSerializer
from .permissions import IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return Task.objects.all().order_by('-created_at')
        if user.is_authenticated:
            return Task.objects.filter(owner=user).order_by('-created_at')
        return Task.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
