from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from . import views

app_name = "news"

router = routers.DefaultRouter()
router.APIRootView.__doc__ = "API for a simple news aggregator"

router.register("comments", views.CommentViewSet)
router.register("posts", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema')
]
