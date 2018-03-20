#database
from models import Snippet
from django.contrib.auth.models import User

#serializer
from snippets.serializers import SnippetSerializer,UserSerializer

#view models
from rest_framework import generics

#permissions
from rest_framework import permissions
from permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):

    #to pass an additional 'owner' field
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    #permission
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    #data
    queryset=Snippet.objects.all()

    #way of serializing
    serializer_class=SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer

class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'snippets':reverse('snippet-list',request=request,format=format)
        })


from rest_framework import renderers

#display highlighted codes in a isolated page
class SnippetHighlight(generics.GenericAPIView):
    queryset=Snippet.objects.all()
    renderer_classes=(renderers.StaticHTMLRenderer,)

    def get(self,request,*args,**kwargs):
        snippet=self.get_object()
        return Response(snippet.highlighted)