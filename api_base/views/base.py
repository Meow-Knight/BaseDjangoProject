from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    serializer_class = None
    required_alternate_scopes = {}
    serializer_map = {}

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
