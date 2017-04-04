from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework import generics

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet
    serializer_class = SnippetSerializer

