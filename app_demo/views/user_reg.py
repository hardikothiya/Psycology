from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from app_demo.models import User, UserTemp
from app_demo.serializers import UserTempSerializer, UserRegSerializer
from rest_framework.response import Response
from .common import send_mail


class UserGetByEmail(APIView):
    """
    """
    def get_object(self, pk):
        try:
            # print(User.objects.filter(id=pk))
            return User.objects.filter(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("ccc")
        snippet = self.get_object(pk)
        print(snippet)

        serializer = UserRegSerializer(
            snippet, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegister(APIView):
    """
    """

    def get(self, request):
        """
        """
        queryset = User.objects.filter()
        serializer = UserRegSerializer(
            queryset, many=True, context={'request': request}
        )
        success = {
            "status": status.HTTP_200_OK,
            "data": serializer.data,
            "message": "User Fetch Successfully"
        }
        return JsonResponse(success, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        """
        try:
            if request.data["password"] == request.data["password2"]:

                serializer = UserRegSerializer(data=request.data)

                if serializer.is_valid():
                    verification_code = send_mail(request.data['email'])
                    # verification_code = 121252
                    request.data['verification_code'] = verification_code

                    userdetail = UserTemp.objects.filter(email=request.data["email"])
                    if userdetail:
                        sv = UserTemp.objects.get(email=request.data['email'])
                        sv.verification_code = verification_code
                        sv.save()
                    else:
                        serializer2 = UserTempSerializer(data={
                            'email': request.data['email'],
                            'verification_code': verification_code
                        })

                        if serializer2.is_valid():
                            serializer2.save()
                    success = {
                        "status": status.HTTP_200_OK,
                        "message": "User OTP saved Successfully"
                    }

                    return JsonResponse(success, status=status.HTTP_200_OK)
                else:
                    error = {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": serializer.errors
                    }
                    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
            else:
                error = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Password Not Match"
                }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = {
                "message": e
            }
            return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)


class check_user_reg_verification_code(APIView):
    """
    """

    def post(self, request):
        print("abcdefghijklm")
        """
        """
        userdetail = UserTemp.objects.filter(email=request.data["email"])

        if userdetail:
            serializer = UserTempSerializer(
                userdetail, many=True, context={'request': request}
            )

            for i in serializer.data:
                print(i)
                if int(request.data["verification_code"]) == int(i['verification_code']):

                    serializer = UserRegSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        success = {
                            "status": status.HTTP_200_OK,
                            "message": "Verify Successfully"
                        }
                        return JsonResponse(success, status=status.HTTP_200_OK)
        success = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Verification Failed",
        }
        return JsonResponse(success, status=status.HTTP_400_BAD_REQUEST)
