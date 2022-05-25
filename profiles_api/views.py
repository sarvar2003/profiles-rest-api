from email import message
from django import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """Test API view"""

    serializer_class = HelloSerializer


    def get(self, reuqest, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View (But specifically intended to be used wih APIs)',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
        
    def post(self, request):
        """Create a  hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST 
                )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method" : 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method' : 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions( list, create, retrieve, update, partial_update)',
            'Automatically maps to URls using Routers',
            'Provide more functionality with less code',
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_response' : 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_response' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_response" : 'PATCH'})

    def destroy(self, reuqest, pk=None):
        """Handle removing an object"""
        return Response({'http_response' : 'DELETE'})
    

class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )


