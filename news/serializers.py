from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post.id')
    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'content', 'creation_date', 'post')
        # fields = ('__all__')
        # extra_kwargs = {
        #     'post': {'lookup_field': 'id'}
        # }

    def create(self, validated_data):
        comment = Comment.objects.create(**{**validated_data, "post": validated_data['post'][
            'id']})

        return comment

    def update(self, instance: Comment, validated_data):
        """The method must to be overridden as I'm probably doing something stupid with all that
        `PrimaryKeyRelatedField` fields stuff...
        """
        if 'post' in validated_data:
            instance.post = validated_data['post']['id']  # actual post instance
            del validated_data['post']

        instance = super().update(instance, validated_data)
        return instance


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    upvotes = serializers.ReadOnlyField()
    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'creation_date', 'author_name', 'upvotes', 'comments')
        # fields = ('__all__')
