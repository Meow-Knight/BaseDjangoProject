from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from api_information.models import User
from api_information.services import UserService


class LoginViewSet(viewsets.ViewSet):

    @action(methods=["post"], detail=False)
    def login(self, request, *args, **kwargs):
        user_data = request.data
        if UserService.is_valid_login_data(user_data):
            user = User.objects.filter(email=user_data.get('email')).first()
            refresh = RefreshToken.for_user(user)

            return Response(
                {"refresh": str(refresh),
                 "access": str(refresh.access_token)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"details": "Email/Password is not correct"},
            status=status.HTTP_400_BAD_REQUEST
        )
