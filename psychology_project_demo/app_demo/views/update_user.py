from rest_framework.views import APIView

from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from app_demo.models import User, UserTemp
from app_demo.serializers import UserUpdateSerializer
from rest_framework.response import Response
from .common import send_mail


class UserUpdate(APIView):
    """
    """

    def post(self, request, *args, **kwargs):
        """
        """
        try:

            serializer = UserUpdateSerializer(data=request.data)
            if serializer.is_valid():
                newdata = request.data
                sv = User.objects.filter(email=request.data["email"])
                if sv:
                    userdata = User.objects.get(email=request.data['email'])
                    userdata.first_name = newdata['first_name']
                    userdata.last_name = newdata['last_name']
                    userdata.gender = newdata['gender']
                    userdata.age = newdata['age']
                    userdata.weight = newdata['wight']
                    userdata.height = newdata['height']

                    userdata.save()
                    success = {
                        "status": status.HTTP_200_OK,
                        "message": "User Data Updated Successfully"
                    }
                    return JsonResponse(success, status=status.HTTP_200_OK)

                else:
                    error = {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": "Incorrect Email"
                    }
                    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)

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
