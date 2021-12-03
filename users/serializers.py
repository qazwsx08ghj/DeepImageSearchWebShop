from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'phoneNum', 'password')

    username = serializers.CharField(
        label='userName', help_text='userName', required=True, allow_blank=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="this user is already exist"
            )
        ]
    )

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True, label='password')

    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """
    User Profile Detail
    """
    class Meta:
        model = User
        fields = ("name", "gender", "b_day", "phoneNum", "email")
