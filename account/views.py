from django.utils import timezone

# Create your views here.
from .serializers import UserSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http.request import QueryDict
from core.authentication import is_authenticate
from core.encryption import jwt_payload_handler, jwt_encode_handler


class UserViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for signup and login users.
    """
    serializer_class = UserSerializer

    def create(self, request):
        """
            To create the User
            URL Structure: /user/signup/
            Required Fields: 'name', 'email', 'phone', 'password'
        """

        data = QueryDict.dict(request.data)
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(new_user.password)
            new_user.save()

            payload = jwt_payload_handler(new_user)
            context = {
                'message': 'User created',
                'token': jwt_encode_handler(payload),
                'user_detail': {
                    'name': new_user.name,
                }
            }
            return Response(context)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def login(request):
        """
            To User login with email and password Authenticates user and returns token
            URL Structure: /user/login/
            Required Fields: {emai l, password}
        """
        email = request.data.get('email')
        password = request.data.get('password')
        user = is_authenticate(email, password)
        if user:
            payload = jwt_payload_handler(user)
            user.last_login = timezone.now()
            user.save()
        else:
            return Response({'message': 'Login Failed'}, status=400)
        context = {
            'token': jwt_encode_handler(payload),
            'user_detail': {
                'name': user.name,
            }
        }
        return Response(context)