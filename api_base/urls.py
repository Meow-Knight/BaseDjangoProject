from rest_framework import routers

from api_base.views import LoginViewSet

app_name = 'api_base'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'', LoginViewSet, basename='login')

urlpatterns = router.urls
