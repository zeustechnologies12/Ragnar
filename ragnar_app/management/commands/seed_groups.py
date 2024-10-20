from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Seed the database with initial groups'

    def handle(self, *args, **kwargs):
        groups = ['manager', 'customer']
        for group_name in groups:
            if not Group.objects.filter(name=group_name).exists():
                Group.objects.create(
                    name=group_name
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created group: {group_name}'))
            else:
                self.stdout.write(self.style.ERROR(f'Group {group_name} already exists'))
