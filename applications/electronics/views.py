from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from applications.comments.mixins import CommentMixin
from applications.electronics.models import Electronic
from applications.electronics.serializers import ElectronicSerializer
from applications.favorites.mixins import FavoriteMixin
from applications.likes.mixins import LikeMixin
from applications.ratings.mixins import RatingMixin
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ElectronicViewSet(FavoriteMixin, CommentMixin, RatingMixin, LikeMixin, ModelViewSet):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['id', 'price']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddElectronicCountAPIView(UpdateAPIView):
    def post(self, request, pk=None):
        electronic = self.get_object()
        amount_to_add = request.data['amount']
        electronic.amount += amount_to_add
        electronic.save()
        return Response({'msg': 'успешно добавлено количество товаров'}, status=status.HTTP_201_CREATED)


