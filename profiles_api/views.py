from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


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
            return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)

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
        
