from rest_framework import serializers
from profiles.models import Profile, ProfileStatus

class ProfileSerializers(serializers.Serializer):
    user = serializers.StringRelatedField(read_only = True)
    avatar = serializers.ImageField(read_only = True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvatarSerializer(serializers.Serializer):
    
    class Meta:
        model = Profile
        fields = "__all__"

class ProfileStatusSerializer(serializers.Serializer):
    user = serializers.StringRelatedField(read_only = True)

    class Meta:
            model = ProfileStatus
            fields = "__all__"