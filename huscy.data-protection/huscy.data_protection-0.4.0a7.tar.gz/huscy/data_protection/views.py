from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from huscy.data_protection.models import DataAccessRequest, DataRevocationRequest
from huscy.data_protection.serializer import (
    DataAccessRequestSerializer,
    DataAccessSerializer,
    DataRevocationRequestSerializer,
)


class RequestPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_superuser


class DataAccessRequestViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                               mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, RequestPermission)
    queryset = DataAccessRequest.objects.all()
    serializer_class = DataAccessRequestSerializer

    @action(detail=True, methods=['POST'], permission_classes=(permissions.IsAdminUser, ))
    def apply(self, request, pk):
        data_access_request = self.get_object()
        serializer = DataAccessSerializer(instance=data_access_request.contact)
        return Response(data=serializer.data)


class DataRevocationRequestViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                                   mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, RequestPermission)
    queryset = DataRevocationRequest.objects.all()
    serializer_class = DataRevocationRequestSerializer

    @action(detail=True, methods=['POST'], permission_classes=(permissions.IsAdminUser, ))
    def apply(self, request, pk):
        data_revocation_request = self.get_object()

        if data_revocation_request.type == DataRevocationRequest.TYPES.get_value('all_data'):
            # TODO: delete attributes, participation requests and participations
            pass

        # TODO: check, if contact is only guardian for a child. then, child must be removed first
        # or needs a new guardian
        data_revocation_request.contact.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
