from rest_framework import serializers

from user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.set_password(user.password)
        user.save()
        UserProfile.objects.create(user=user)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email


class NewsFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFeed
        fields = "__all__"


