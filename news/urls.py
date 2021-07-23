from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "news"

router = routers.DefaultRouter()
router.APIRootView.__doc__ = "API for a simple news aggregator"

router.register("comments", views.CommentViewSet)
router.register("posts", views.PostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
