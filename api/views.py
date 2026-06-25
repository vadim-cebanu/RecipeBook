from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime
from .serializers import HelloSerializer


class HelloViewSet(viewsets.ViewSet):
    """
    Sample ViewSet to test the API
    """
    
    def list(self, request):
        data = {
            'message': 'Welcome to your Django REST Framework API!',
            'timestamp': datetime.now()
        }
        serializer = HelloSerializer(data)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def status(self, request):
        return Response({
            'status': 'operational',
            'message': 'API is working perfectly!',
            'timestamp': datetime.now()
        })
