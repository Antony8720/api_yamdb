from django.shortcuts import render
from reviews.models import Comment, Review
from rest_framework import (viewsets,
                            permissions,
                            filters,
                            mixins)
from .serializers import (CommentSerializer,
                          ReviewSerializer)
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import mixins, filters, viewsets
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import AdminOnlyPermission, SafeMethodOnlyPermission
from api.serializers import GenreSerializer, CategorySerializer, \
    TitleSerializer
from reviews.models import Title, Genre, Category


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=id)
        new_queryset = title.reviews.all()
        return new_queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=id)
        new_queryset = review.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)



class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
#    filter_backends = (DjangoFilterBackend,)
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminOnlyPermission,)


class GenreViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.CreateModelMixin
                   ):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    pagination_class = LimitOffsetPagination
    permission_classes = (SafeMethodOnlyPermission,)


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin
                      ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    pagination_class = LimitOffsetPagination
    permission_classes = (SafeMethodOnlyPermission,)

