from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from . import serializers
from .permissions import isDoctor, isHospital


class DoctorSignupView(generics.GenericAPIView):
    serializer_class = serializers.DoctorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class HospitalSignupView(generics.GenericAPIView):
    serializer_class = serializers.HospitalSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'role': user.role
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class DoctorOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & isDoctor]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user


class HospitalOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & isHospital]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
