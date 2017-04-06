from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

from rest_framework import generics

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    """
    List all snippets
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

