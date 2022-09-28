from rest_framework.views import APIView

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

            serializer = ContactUsSerializer(data=request.data)
            if serializer.is_valid():
                sv = ContactUsSerializer.objects.filter(email=request.data["email"])
                sv.save()

                success = {
                    "status": status.HTTP_200_OK,
                    "data": serializer.data,
                    "message": "Request submitted Successfully"
                }
                return JsonResponse(success, status=status.HTTP_200_OK)
            else:
                error = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": serializer.errors
                }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = {
                "message": e
            }
            return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
