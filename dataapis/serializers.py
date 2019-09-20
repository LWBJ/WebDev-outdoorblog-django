from rest_framework import serializers
from dataapis.models import OutdoorDate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class OutdoorDateSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = OutdoorDate
    fields = ['pk', 'title', 'place', 'date', 'description', 'comments', 'picture', 'owner', 'url']
    
class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'username',]
    

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')
       