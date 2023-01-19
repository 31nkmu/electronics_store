from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.likes import services


class LikeMixin:
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        user = request.user
        status_ = services.like_unlike(user=user, obj=obj)
        return Response({'status': status_, 'user': user.email}, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def fans(self, request, pk=None):
        obj = self.get_object()
        return Response(services.get_fans(obj=obj), status=status.HTTP_200_OK)
