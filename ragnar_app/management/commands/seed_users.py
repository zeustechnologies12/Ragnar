from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Seed the database with initial users'

    def handle(self):
        # Check if users already exist
        if not User.objects.filter(username='admin').exists():
            # Create a superuser
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='adminpassword'
            )
            self.stdout.write(self.style.SUCCESS('Successfully created admin user'))
        else:
            self.stdout.write(self.style.ERROR('Test user already exists'))
