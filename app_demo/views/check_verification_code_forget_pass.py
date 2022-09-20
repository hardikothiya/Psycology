from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from app_demo.models import User
from app_demo.serializers import UserRegSerializer


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
        success = {
            "status": status.HTTP_200_OK,
            "message": "FORGETPASS_SUCCESS",
            "msgcode": "Success"
        }
        return JsonResponse(success, status=status.HTTP_200_OK)