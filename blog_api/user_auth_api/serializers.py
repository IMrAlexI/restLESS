from user_auth_api.models import User
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'url')
        extra_kwargs = {'password' : {'write_only' : True}}

        def create(self, validated_data):
            user = User(**validated_data)
            password = validated_data.pop('password')
            gen_u_name = validated_data.pop('email')
            user.username = gen_u_name
            user.set_password(password)
            user.save()
            return user
