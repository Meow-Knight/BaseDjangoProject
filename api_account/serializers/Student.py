from rest_framework import serializers

from api_account.models import Student
from api_account.serializers import AccountSerializer
from api_account.services import AccountService


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentRegisterSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        account_data = validated_data.get("account")
        account = AccountService.create_account(account_data)
        validated_data['account'] = account
        return super().create(validated_data)
