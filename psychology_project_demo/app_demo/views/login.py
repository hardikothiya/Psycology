from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from app_demo.models import User
from app_demo.serializers import UserRegSerializer


class Login(APIView):
    """
    """
    def post(self, request):
        """
        """
        try:
            userdetail = User.objects.filter(email=request.data["email"])
            if userdetail:
                serializer = UserRegSerializer(
                    userdetail, many=True, context={'request': request}
                )
                for i in serializer.data:
                    if str(request.data["password"]) ==  str(i['password']):
                        success = {
                            "status": status.HTTP_200_OK,
                            "data": serializer.data,
                            "message": "Login Successfully"
                        }
                        return JsonResponse(success, status=status.HTTP_200_OK)
                    else:
                        errror = {
                            "status": status.HTTP_400_BAD_REQUEST,
                            "data": [],
                            "message": "Invalid Password"
                        }
                        return JsonResponse(errror, status=status.HTTP_200_OK)
            else:
                errror = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "data": [],
                    "message": "User Not Found"
                }
                return JsonResponse(errror, status=status.HTTP_200_OK)
        except Exception as e:
            errror = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": str(e)
            }
            return JsonResponse(errror, status=status.HTTP_200_OK)