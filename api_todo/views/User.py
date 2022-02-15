from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination

from api_todo.models import User
from api_todo.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error_message": "Username existed"}, status=status.HTTP_400_BAD_REQUEST)

        account = User(username=username, password=password)
        account.save()

        return Response(UserSerializer(account).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signin(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username, password=password)

        if user.exists():
            user = user.first()
            token = RefreshToken.for_user(user)
            response = {
                'access_token': str(token.access_token),
                'refresh_token': str(token)
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"error_message": "invalid username/password"}, status=status.HTTP_400_BAD_REQUEST)
