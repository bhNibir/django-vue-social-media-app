from rest_framework import serializers
#from .models impo
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Post

# this will handle our backend data, allows python to understand complex data and later can send data to frontend
# need to make a serializer for every model
# they are classes you need to define, and use rest framework to automatically create serializer for the model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userfields = ('id','username','password')
        extra_kwargs = {'password':{'required':True, 'write_only':True}}

        def create(self, validted_data): # we need to assign token to a user to validate user for frontend
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','content','user')            