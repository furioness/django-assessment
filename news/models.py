from django.db import models


class Post(models.Model):
    title = models.TextField()
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.TextField()
    upvotes = models.IntegerField(default=0)


class Comment(models.Model):
    author_name = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

