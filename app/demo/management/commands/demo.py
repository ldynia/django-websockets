from demo.models import Person
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Demo command'

    def handle(self, *args, **options):
        p, created = Person.objects.get_or_create(
            first_name='John',
            last_name='Lennon',
        )
        p = Person.objects.first()
        p.first_name = 'Foo'
        p.last_name = 'Barr'
        p.save()
        print('Person updated')
