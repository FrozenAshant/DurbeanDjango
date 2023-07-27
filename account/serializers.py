from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    # we need confirm password field in our Registration Request
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # validate password and confirm password while registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise ValueError("Password and Confirm Password does not match")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    # mention email
    email = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]