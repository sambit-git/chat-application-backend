from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
class LogoutAPIView(GenericAPIView):
    queryset = Token.objects.all()

    def get(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        print(token)
        token.delete()
        return Response(
            {"detail": "Logout successful"},
            status=status.HTTP_200_OK)
