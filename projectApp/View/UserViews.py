# UserViews.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from projectApp.Serializer import UserSerializer
from projectApp.models import User


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return Response({'message': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
            if password==user.password:
                return Response({'message': 'You have successfully logged in'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class ChangePasswordView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        new_password = data.get('new_password')

        if not email or not password or not new_password:
            return Response({'message': 'Email, old password, and new password are required'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        # Check if old password is correct
        if password!=user.password:
            return Response({'message': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        # Update password
        user.password = new_password
        user.save()
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)


