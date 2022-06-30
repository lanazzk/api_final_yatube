from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import OwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          OwnerOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          OwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        get_object_or_404(Post, id=post_id)
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class ListCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(ListCreateViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('^following__username',)

    def get_queryset(self):
        follow = Follow.objects.filter(user=self.request.user)
        return follow

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
