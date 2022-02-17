from django.contrib.auth.hashers import check_password, make_password
from rest_framework_simplejwt.tokens import RefreshToken

from api_account.models import Account


class AccountService:

    @classmethod
    def login_with_username_password(cls, username, password, account_type):
        account = Account.objects.filter(username=username, role_id=account_type.value['id'])
        if account.exists():
            account = account.first()
            if check_password(password, account.password):
                token = RefreshToken.for_user(account)
                return {
                    "account_id": account.id,
                    "access_token": str(token.access_token),
                    "refresh_token": str(token)
                }
        return None

    @classmethod
    def create_account(cls, account_data):
        password = account_data.get("password")
        if not password:
            return None
        account_data['password'] = make_password(password)
        return Account.objects.create(**account_data)
