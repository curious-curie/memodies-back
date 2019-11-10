from django.conf.urls import url
from .views import PostViewSet, RegistrationAPI, LoginAPI, UserAPI
from knox import views as knox_views

post_list =PostViewSet.as_view({"get": "list", "post": "create"})
post_detail =PostViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
)


urlpatterns = [
    url("posts/$", post_list, name="post-list"),
    url("^posts/(?P<pk>[0-9]+)/$", post_detail, name="post-detail"),
    # url("auth/logout/", knox_views.LogoutView.as_view(), name='knox_logout'),
    url("^auth/register/$", RegistrationAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
]