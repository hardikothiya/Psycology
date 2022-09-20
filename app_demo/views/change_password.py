import random
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from app_demo.models import User
from app_demo.serializers import UserRegSerializer


class changepassword(APIView):
    """
    """
    def post(self, request):
        """
        """
        try:
            userdetail = User.objects.filter(id=request.data["id"])
            if userdetail:
                serializer = UserRegSerializer(
                    userdetail, many=True, context={'request': request}
                )
                for i in serializer.data:
                    userid = i['id']
                    email = i['email']
                    verifycode = random.randrange(111111, 999999, 6)
                    userdata = User.objects.get(id=userid)
                    userdata.verification_code = verifycode
                    userdata.save()
                    success = {
                        "status": status.HTTP_200_OK,
                        "message": "Verification code sent on your mail. please verify",
                        "msgcode": "Success"
                    }
                    return JsonResponse(success, status=status.HTTP_200_OK)
            else:
                errror = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "User Not Found",
                    "msgcode": "Fail"
                }
                return JsonResponse(errror, status=status.HTTP_200_OK)
        except Exception as e:
            errror = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": str(e),
                "msgcode": "Fail"
            }
            return JsonResponse(errror, status=status.HTTP_200_OK)


class verify_change_password(APIView):
    """
    """
    def post(self, request):
        """
        """
        try:
            userdetail = User.objects.filter(id=request.data["id"])
            if userdetail:
                serializer = UserRegSerializer(
                    userdetail, many=True, context={'request': request}
                )
                for i in serializer.data:
                    userid = i['id']
                    if i['verification_code'] == request.data['verification_code']:
                        userdata = User.objects.get(id=userid)
                        userdata.password = request.data['password']
                        userdata.save()
                        success = {
                            "status": status.HTTP_200_OK,
                            "message": "change password verify code success",
                            "msgcode": "Success"
                        }
                        return JsonResponse(success, status=status.HTTP_200_OK)
                    else:
                        error_response = {
                            "status": status.HTTP_400_BAD_REQUEST,
                            "message": "change password verify code Wrong",
                            "msgcode": "Fail"
                        }
                        return JsonResponse(error_response, status=status.HTTP_400_BAD_REQUEST)
            else:
                error_response = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "User NOt Found",
                    "msgcode": "Fail"
                }
                return JsonResponse(error_response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": str(e),
                "msgcode": "Fail"
            }
            return JsonResponse(error_response, status=status.HTTP_400_BAD_REQUEST)
