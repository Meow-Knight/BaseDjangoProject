from rest_framework import routers

from api_todo.views import UserViewSet, NoteViewSet

app_name = 'api_todo'

router = routers.SimpleRouter(trailing_slash=True)

router.register(r'user', UserViewSet, basename='user')
router.register(r'note', NoteViewSet, basename='note')

urlpatterns = router.urls
