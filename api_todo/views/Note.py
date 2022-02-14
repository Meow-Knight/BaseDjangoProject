from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_todo.models import Note
from api_todo.serializers.Note import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @action(detail=False, methods=['post'])
    def list_note_by_user(self, request):
        username = request.data.get('username');

        notes = Note.objects.filter(user__username=username)
        if notes.exists():
            return Response(NoteSerializer(notes).data, status=status.HTTP_200_OK)
        else:
            return Response({"error_message": "error in find list notes by user"}, status=status.HTTP_400_BAD_REQUEST)
