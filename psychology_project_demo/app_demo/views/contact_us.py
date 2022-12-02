
from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from app_demo.serializers import ContactUsSerializer
from rest_framework.response import Response
from .common import send_mail


class ContactUs(APIView):
    """
    """

    def post(self, request, *args, **kwargs):
        """
        """
        try:
            print('data --', request.data)
            serializer = ContactUsSerializer(data=request.data)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                success = {
                    "status": status.HTTP_200_OK,
                    "data": serializer.data,
                    "message": "Request submitted Successfully"
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
