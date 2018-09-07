# !/usr/bin/env python .
# Created Wednesday, August 15, 2018 .
# Blender 2.79 profileserializer.py
# Dictionary Loader .
# Last update :
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('company', 'is_admin', 'last_modified', 'uuid')

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user
