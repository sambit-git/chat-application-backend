from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class LogoutAPIView(GenericAPIView):
    queryset = Token.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        print(token)
        token.delete()
        return Response(
            {"detail": "Logout successful"},
            status=status.HTTP_200_OK)

class ValidateLoggedInAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user_serializer = UserSerializer(request.user)
        return Response( user_serializer.data, status=status.HTTP_200_OK )
