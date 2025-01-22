from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserRegisterTokenSerializer
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
class UserRegisterView(APIView):
    def post(self, request, format=None):
        data = request.data
        username = data['username']
        email = data['email']

        if username == "" or email == "":
            return Response({"detail": "Username or email cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            username_exists = User.objects.filter(username=username).count()
            email_exists = User.objects.filter(email=email).count()

            if username_exists:
                error_message = "A user with that username already exists!"
                return Response({"detail": error_message}, status=status.HTTP_403_FORBIDDEN)
            if email_exists:
                error_message = "A user with that email already exists!"
                return Response({"detail": error_message}, status=status.HTTP_403_FORBIDDEN)

            user = User.objects.create(username=username, email=email, password=make_password(data["password"]),)
            serializer = UserRegisterTokenSerializer(user, many=False)
            return Response(serializer.data)
                