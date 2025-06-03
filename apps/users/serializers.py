from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name",
                  "is_active", "is_staff", "date_joined",
                  ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["email", "username", "password", "first_name", "last_name"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered"
            )
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    user = UserDetailSerializer(read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("User is inactive")

        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserDetailSerializer(user).data,
        }


class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, data):
        try:
            refresh = RefreshToken(data["refresh"])
            return {"access": str(refresh.access_token)}
        except Exception:
            raise serializers.ValidationError("Invalid refresh token")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name", "is_active",
            "is_staff", "date_joined",
        ]
