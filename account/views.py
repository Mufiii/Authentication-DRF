from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework import status
from django.contrib.auth import authenticate
from .renders import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken

# Generate Token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Registration
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
      serializer = UserRegistrationSerializer(data = request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response({'msg':'Registration Done Successfully'},status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#Login   
class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self,request,format=None):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
      email = serializer.data.get('email')
      password = serializer.data.get('password')
      user = authenticate(email=email,password=password)
      if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token,'msg':'Login Successful'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'non_field_errors':['Email or Password is Not Valid']}},
                          status=status.HTTP_400_BAD_REQUEST)

    