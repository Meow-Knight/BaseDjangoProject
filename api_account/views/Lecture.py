from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.constants import RoleData
from api_account.models import Lecture
from api_account.serializers import LectureSerializer, LectureRegisterSerializer
from api_account.services import AccountService
from api_base.views import BaseViewSet


class LectureViewSet(BaseViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        lecture_data = request.data

        if not lecture_data.get("account"):
            return Response({"error_message": "account is required"}, status=status.HTTP_400_BAD_REQUEST)
        lecture_data['account']['role'] = RoleData.LECTURE.value['id']
        serializer = LectureRegisterSerializer(data=lecture_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            token_data = AccountService.login_with_username_password(lecture_data['account']['username'],
                                                                     lecture_data['account']['password'],
                                                                     RoleData.LECTURE)
            return Response(token_data, status= status.HTTP_200_OK)
