from django.shortcuts import render
from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import (PostSerializer, CreateUserSerializer,
    UserSerializer,
    LoginUserSerializer,
    PlaylistSerializer,
)
from knox.models import AuthToken 
from memodies.models import Post, Playlist
from django.contrib.auth.models import User
# from serializers import PostSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        print(self.request.user)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    
    def get_queryset(self):
        return Playlist.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.request.data['track'])
        serializer.save(owner = self.request.user, track=post)
       


class PlaylistFilter(generics.ListAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        user = self.kwargs['username']
        return Playlist.objects.filter(owner=user).order_by("-created_at")

    