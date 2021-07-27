from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post, Comment


class InvalidateExtraFieldsMixin:
    """Mixin for disallowing extra fields in user's input data.
    From https://stackoverflow.com/a/31412477"""

    def is_valid(self, raise_exception=False):
        if hasattr(self, "initial_data"):
            payload_keys = self.initial_data.keys()  # all the payload keys
            serializer_fields = self.fields.keys()  # all the serializer fields
            extra_fields = [
                extra_key
                for extra_key in payload_keys
                if extra_key not in serializer_fields
            ]
            if extra_fields:
                raise ValidationError(f"Extra fields {extra_fields} in payload")
        return super().is_valid(raise_exception)


class CommentSerializer(
    InvalidateExtraFieldsMixin, serializers.HyperlinkedModelSerializer
):
    post = serializers.PrimaryKeyRelatedField(source="post.id", read_only=True)
    # TODO: must raise an error if read-only provided

    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ("id", "author_name", "content", "creation_date", "post")


class CommentSerializerForCreation(CommentSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source="post.id"
    )

    def create(self, validated_data):
        comment = Comment.objects.create(
            **{**validated_data, "post": validated_data["post"]["id"]}
        )
        return comment


class PostSerializer(InvalidateExtraFieldsMixin, serializers.ModelSerializer):
    comments = CommentSerializerForCreation(many=True, read_only=True)
    upvotes = serializers.ReadOnlyField()
    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "author_name",
            "upvotes",
            "comments",
        )
