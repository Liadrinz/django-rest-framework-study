 #database
from models import Snippet
from django.contrib.auth.models import User

#serializer
from snippets.serializers import SnippetSerializer,UserSerializer

#view models
from rest_framework import generics
from rest_framework import viewsets

#permissions
from rest_framework import permissions
from permissions import IsOwnerOrReadOnly

#
from rest_framework.decorators import detail_route
from rest_framework.response import Response

#
from rest_framework import renderers

class SnippetViewSet(viewsets.ModelViewSet):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        snippet=self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

