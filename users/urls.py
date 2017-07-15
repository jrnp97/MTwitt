from django.conf.urls import url
from .views import index, profile
from django.contrib.auth.decorators import login_required

app_name="user"
urlpatterns = [
    url(r'^$', index.as_view(), name="index"),
    url(r'^profile/', login_required(profile.as_view()), name="profile")
]