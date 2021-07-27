from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(source="post.id", read_only=True)
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


class PostSerializer(serializers.ModelSerializer):
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
