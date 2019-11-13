from memodies.models import Post, Playlist
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(source = 'owner.username', read_only = True)
    class Meta:
        model = Post
       
        # owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('id', 'title', 'artist', 'album', 'memo', 'artwork', 'preview', 'owner')
        
    
  
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user




class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


class PlaylistSerializer(serializers.ModelSerializer):
    # owner = serializers.CharField(source = 'owner.username', read_only = True)
    owner = UserSerializer(read_only=True)
    track = PostSerializer(read_only=True)
    class Meta:
        model = Playlist
        fields = ('id', 'owner', 'track')

    # def perform_create(self, validated_data):
    #     post = Post.objects.get(pk = validated_data)
    #     playlist = Playlist.objects.create(post)
    #     playlist.save()
    #     return playlist        