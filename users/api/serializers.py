from rest_framework import serializers

from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'email']


class DoctorSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = models.User
        fields = ['username', 'email', 'role', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = models.User(
            username=self.validated_data['username'],
            email=self.validated_data['email']

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "Password mismatch"})
        user.set_password(password)
        user.role = "doctor"
        user.save()
        models.Doctor.objects.create(user=user)
        return user


class HospitalSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = models.User
        fields = ['username', 'email', 'role', 'password', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = models.User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "Password mismatch"})
        user.set_password(password)
        user.role = "hospital"
        user.save()
        models.Hospital.objects.create(user=user)
        return user
