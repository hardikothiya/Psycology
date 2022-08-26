import random
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from app_demo.models import User
from app_demo.serializers import UserRegSerializer


class Forget_password(APIView):
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
                    userid = i['id']
                    verifycode = random.randrange(111111, 999999, 6)
                    userdata = User.objects.get(email=request.data["email"], id=userid)
                    userdata.verification_code = verifycode
                    userdata.save()
                    success = {
                        "status": status.HTTP_200_OK,
                        "message": "code send successfully",
                        "msgcode": "Success"
                    }
                    return JsonResponse(success, status=status.HTTP_200_OK)
            else:
                errror = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "FORGETPASS_FAIL",
                    "msgcode": "Error"
                }
                return JsonResponse(errror, status=status.HTTP_200_OK)
        except Exception as e:
            errror = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": str(e)
            }
            return JsonResponse(errror, status=status.HTTP_200_OK)

class check_Forget_password_verification_code(APIView):
    """
    """
    def post(self, request):
        print("abcdefghijklm")
        """
        """
        userdetail = User.objects.filter(email=request.data["email"])
        print(userdetail)
        if userdetail:
            serializer = UserRegSerializer(
                userdetail, many=True, context={'request': request}
            )
            for i in serializer.data:
                if int(request.data["verification_code"]) == int(i['verification_code']):
                    success = {
                        "status": status.HTTP_200_OK,
                        "message": "Verify Successfully"
                    }
                    return JsonResponse(success, status=status.HTTP_200_OK)
                else:
                    success = {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": "Invalid Otp",
                        "msgcode": "Success"
                    }
                    return JsonResponse(success, status=status.HTTP_200_OK)

        else:
            success = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "User not Found",
                "msgcode": "Success"
            }
            return JsonResponse(success, status=status.HTTP_200_OK)

class resendforgetcode(APIView):
    """
    """
    def post(self, request):
        userdetail = User.objects.filter(email=request.data["email"])
        if userdetail:
            serializer = UserRegSerializer(
                userdetail, many=True, context={'request': request}
            )
            for i in serializer.data:
                verification_code = i['verification_code']
                print(verification_code)
                success = {
                    "status": status.HTTP_200_OK,
                    "message": "Resend Verification Successfully"
                }
                return JsonResponse(success, status=status.HTTP_200_OK)
        else:
            errror = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "User Not Found",
                "msgcode": "Fail"
            }
            return JsonResponse(errror, status=status.HTTP_200_OK)

class setpassword(APIView):
    """
    """
    def post(self, request):
        """
        """
        try:
            userdetail = User.objects.get(email=request.data["email"])
            if userdetail:
                if str(request.data["password"]) == str(request.data["password2"]):
                    userdetail.password = str(request.data["password"])
                    userdetail.save()
                    success = {
                        "status": status.HTTP_200_OK,
                        "message": "Password change Successfully",
                        "msgcode": "Success"
                    }
                    return JsonResponse(success, status=status.HTTP_200_OK)
                else:
                    errror = {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": "Passsword Mismatch",
                        "msgcode": "Fail"
                    }
                    return JsonResponse(errror, status=status.HTTP_200_OK)
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