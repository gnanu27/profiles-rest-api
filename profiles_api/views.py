from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """Return an list of  APIView features """
        an_apiview = [
        'uses HTTP methods as function (get, post, patch, put, delete)',
        'is Similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'is mapped mauelly to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
