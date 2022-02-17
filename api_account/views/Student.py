from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.constants import RoleData
from api_account.models import Student
from api_account.serializers import StudentSerializer, StudentRegisterSerializer
from api_account.services import AccountService
from api_base.views import BaseViewSet


class StudentViewSet(BaseViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        student_data = request.data

        if not student_data.get('account'):
            return Response({"error_message": "account is required!! "}, status=status.HTTP_400_BAD_REQUEST)
        student_data['account']['role'] = RoleData.STUDENT.value['id']
        serializer = StudentRegisterSerializer(data=student_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            token_data = AccountService.login_with_username_password(student_data['account']['username'],
                                                                    student_data['account']['password'],
                                                                    RoleData.STUDENT)

        return Response(token_data, status=status.HTTP_200_OK)



