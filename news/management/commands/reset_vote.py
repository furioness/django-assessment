from django.core.management.base import BaseCommand
from news.models import Post


class Command(BaseCommand):
    help = "Reset votes on all news"

    def handle(self, *args, **options):
        Post.objects.update(upvotes=0)
        self.stdout.write("Vote resetting is done.")
        return  # recommended by a link...
        # https://devcenter.heroku.com/articles/scheduling-custom-django-management-commands
