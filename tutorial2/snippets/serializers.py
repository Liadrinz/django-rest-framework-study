from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

#this module uses Serializers inherited from serializer.ModelSerializer

class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    #serialize owner as Read-Only and put username of owner into the JSON instead of the default attribute
    #if not, the owner can be changed randomly and the value of 'owner' in JSON is the owner_id
    owner=serializers.ReadOnlyField(source='owner.username')

    highlight=serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')

    class Meta:
        model=Snippet #the following fields are built based on class Snippet in models
        fields=('url','id','highlight','title','code','linenos','language','style','owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    #snippets are not originally included in the User model
    snippets=serializers.HyperlinkedIdentityField(many=True,view_name='snippet-detail',read_only=True)
    
    class Meta:
        model=User
        fields=('url','id','username','snippets')


