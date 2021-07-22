from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post.id')

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


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'creation_date', 'author_name', 'upvotes', 'comments')
        # fields = ('__all__')



