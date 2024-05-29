from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContentSerializer
from .models import Content


class ContentViewSet(APIView):   
    """
    A ViewSet for retrieving and creating content objects.
    """
    def get(self, request, format=None):
        """
        Handles GET requests to retrieve a list of all content objects.
            1. retrieves all content objects from the database.
            2 Serializes the list of content objects.
            3. returns the serialized data as a JSON response.
        Args:
            request: The incoming HTTP request object.
            format: The format of the response (None by default).
        Returns:
            Response: A JSON response with the list of content objects.
        """
        content_list = Content.objects.all()
        serializer = ContentSerializer(content_list, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        """
        Handles POST requests to create a new content object.
            1. deserializes the received data.
            2. checks the validity of the deserialized data.
            3. saves the new content object if the data is valid
            4. returns a JSON response with the created content object and the HTTP status 201.
            5. returns a JSON response with errors and the HTTP status 400 if the data is invalid.
        Args:
            request: The incoming HTTP request object.
            format: The format of the response (None by default).
        Returns:
            Response: A JSON response with the created content object or the validation errors.
        """
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)