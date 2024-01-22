from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
