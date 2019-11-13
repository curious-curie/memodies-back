from django.conf.urls import url
from .views import PlaylistViewSet, PlaylistFilter, PostViewSet, RegistrationAPI, LoginAPI, UserAPI, UserViewSet
from knox import views as knox_views
from rest_framework import routers

post_list =PostViewSet.as_view({"get": "list", "post": "create"})
post_detail =PostViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
)

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

playlist_list = PlaylistViewSet.as_view({"get": "list", "post": "create"})
playlist_detail = PlaylistViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
)

# router = routers.DefaultRouter()
# router.register(r'playlists', PlaylistViewSet)
# router.register(r'playlist/(?P<author_id>\d+)/?$', PlaylistFilter, base_name="playlist_by_user")


urlpatterns = [
    url("posts/$", post_list, name="post-list"),
    url("^posts/(?P<pk>[0-9]+)/$", post_detail, name="post-detail"),
    # url("auth/logout/", knox_views.LogoutView.as_view(), name='knox_logout'),
    url("^auth/register/$", RegistrationAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^playlists/$', playlist_list, name='playlist'),
    url(r'playlists/(?P<pk>[0-9]+)/$', playlist_detail, name='playlist-detail'),
    url('pl/(?P<username>\w+)/$', PlaylistFilter.as_view(), name='playlist_user' )

]