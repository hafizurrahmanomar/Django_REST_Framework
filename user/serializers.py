from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')

    def create(self, data):
        model = get_user_model()
        user = model.objects.create_user(**data)
        return user

    def update(self, instance, data):
        user = super().update(instance, data)

        password = data.pop('password', None)
        if password:
            user.set_password(password)
            user.save()

        return user

    def delete(self, instance):
        instance.delete()
        return {'message': 'User deleted!'}


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError("Incorrect credentials", code='authentication')

        attrs['user'] = user
        return attrs
