from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test API view"""

    def get(self, reuqest, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View (But specifically intended to be used wih APIs)',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
        