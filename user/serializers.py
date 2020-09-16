from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password2 = serializers.CharField(label='Confirm Password', write_only=True)
    def validate(self, attrs):
        #pop password2 out attrs to prevent it come in to User()
        password2 = attrs.pop("password2")
        if (attrs['email'] and User.objects.filter(email=attrs['email']).exists()):
            raise serializers.ValidationError({'email': 'Email addresses must be unique.'})
        if attrs['password'] != password2:
            raise serializers.ValidationError({'password': 'Two password are the differ.'})
        return attrs
    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')
        def create(self, validated_data):
             email = validated_data.get('email')
             username = validated_data.get('username')
             password = validated_data.get('password')
             try:
                 user = User.objects.create(username=username, email=email)
                 user.set_password(password)
                 user.save()
                 return user
             except Exception as e:
                 return e

    