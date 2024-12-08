from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=255)
    mobile = serializers.CharField(max_length=15)
    pincode = serializers.CharField(max_length=6, allow_null=True)
    profile_image = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'location', 'mobile', 'pincode', 'profile_image']

    def create(self, validated_data):
        location = validated_data.pop('location')
        mobile = validated_data.pop('mobile')
        pincode = validated_data.pop('pincode',None)
        profile_image = validated_data.pop('profile_image', None)

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )

        user_profile = UserProfile.objects.create(
            user=user,
            location=location,
            mobile=mobile,
            pincode=pincode,
            profile_image=profile_image
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, atr):
        username = atr.get('username')
        password = atr.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            return atr
        raise serializers.ValidationError('Invalid username or password')
