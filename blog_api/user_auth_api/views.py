from .models import User
from .serializers import UserProfileSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class HelloWorldView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request):
        content = {'message' : 'Hello World! My greetings!'}
        return Response(content)
