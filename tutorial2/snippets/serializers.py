from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snippet#the following fields are built based on class Snippet in models
        fields=('id','title','code','linenos','language','style','owner')
    owner=serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields('id','username','snippets')

