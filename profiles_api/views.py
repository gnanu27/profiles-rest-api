from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Return an list of  APIView features """
        an_apiview = [
        'uses HTTP methods as function (get, post, patch, put, delete)',
        'is Similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'is mapped mauelly to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """
            create Hello Message with name
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Handle updating the objects
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Handle partial update of an objects
        """

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Handle deleting the objects
        """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """
        Test API viewsets
    """
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return Hello Message"""
        an_viewset = [
            'uses  actions(list, create, retrive, update, partial_update)',
            'Automatically maps to URLS using Router',
            'Provides more functionality with less code']

        return Response({'message': 'Hello', 'a_viewset': an_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            message = f'Hello {name}'
            
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """
        Handle Creating and updating Profiles
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
