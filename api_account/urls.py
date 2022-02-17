from rest_framework import routers

from api_account.views import StudentViewSet, AccountViewSet
from api_account.views import LectureViewSet

app_name = 'api_account'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'student', StudentViewSet, basename='student')
router.register(r'lecture', LectureViewSet, basename='lecture')
router.register(r'account', AccountViewSet, basename='account')

urlpatterns = router.urls
