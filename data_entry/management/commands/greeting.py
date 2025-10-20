from django.core.management.base import BaseCommand


# Proposed command = python manage.py greeting Name
# Proposed output = Good morning, {Name}
class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies user name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Good morning, {name}'
        self.stdout.write(self.style.WARNING(greeting))
        # error message
        # self.stderr.write(greeting)
