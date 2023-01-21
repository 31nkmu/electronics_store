from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from applications.electronics.mixins import CharAmountMixin
from applications.electronics.models import Electronic, Characteristic
from applications.electronics.permissions import IsSellerOrReadOnly
from applications.electronics.serializers import ElectronicSerializer, CharacteristicSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from applications.feedback.mixins import FavoriteMixin, CommentMixin, RatingMixin, LikeMixin


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ElectronicViewSet(FavoriteMixin, CommentMixin, RatingMixin, LikeMixin, CharAmountMixin, ModelViewSet):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializer
    permission_classes = [IsSellerOrReadOnly]
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['id', 'price']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
