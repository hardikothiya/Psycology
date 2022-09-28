from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from ..models import Mood as mood1
from ..serializers import MoodSerializer
from rest_framework.response import Response
from .common import send_mail

class Mood1(APIView):
    def get_object(self, pk):
        try:
            return mood1.objects.filter(userid=1)
        except mood1.DoesNotExist:
            raise Http404

    def get(self, request, pk, ):
        print('-----', pk)
        snippet = self.get_object(pk)
        serializer = MoodSerializer(
            snippet, many=True, context={'request': request}
        )
        return Response(serializer.data)

class Mood(APIView):
    """
    """

    def post(self, request, *args, **kwargs):
        """
        """
        try:
            print(request.data)
            serializer = MoodSerializer(data=request.data)
            if serializer.is_valid():

                serializer.save()
                success = {
                    "status": status.HTTP_200_OK,
                    "data": serializer.data,
                    "message": "Mood submitted Successfully"
                }
                return JsonResponse(success, status=status.HTTP_200_OK)
            else:
                print('serializer.errors')
                error = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": serializer.errors
                }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = {
                "message": 'Enter valid details'
            }
            return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
