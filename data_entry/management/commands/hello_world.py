from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print Hello World"

    def handle(self, *args, **kwargs):
        # all the logic that needs to be performed when running this command
        self.stdout.write('hello world')