from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password", "")
        validated_data["password"] = make_password(password)

        new_password = User.objects.create(**validated_data)
        return new_password

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.introduction = validated_data.get(
            "introduction", instance.introduction
        )
        instance.gender = validated_data.get("gender", instance.gender)
        password = validated_data.pop("password", "")
        validated_data["password"] = make_password(password)
        password = User.objects.create(**validated_data)
        instance.save()
        return instance
