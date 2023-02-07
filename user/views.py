from rest_framework import generics, status
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer, SignupSerializer


# Create your views here.
class UserView(generics.ListAPIView):
	queryset = User.objects.all().order_by('first_name')
	serializer_class = UserSerializer
	pagination_class = LimitOffsetPagination

	def get_queryset(self):
		excludeUsersArr = []
		try:
			excludeUsers = self.request.query_params.get('exclude')
			if excludeUsers:
				userIds = excludeUsers.split(',')
				for userId in userIds:
					excludeUsersArr.append(int(userId))
		except:
			return []
		return super().get_queryset().exclude(id__in=excludeUsersArr)


class LoginApiView(TokenObtainPairView):
	authentication_classes = (authentication.BasicAuthentication, authentication.SessionAuthentication)
	permission_classes = [AllowAny]
	serializer_class = TokenObtainPairSerializer

	def post(self, request, *args, **kwargs):
		print("Requesrt = ", request)
		response = super().post(request, *args, **kwargs)

		if response.status_code == status.HTTP_200_OK:
			# Save the token to the database
			user = request.user
			# Retrieve existing token for the user
			token, created = Token.objects.get_or_create(user=user)
			# Use the existing token if it exists, otherwise create a new one
			response.data["token"] = token.key

		return response


class SignupApiView(generics.CreateAPIView):
	permission_classes = [AllowAny]
	queryset = User.objects.all()
	serializer_class = SignupSerializer


def logout_user(request):
    logout(request)
    return HttpResponse('Logout')