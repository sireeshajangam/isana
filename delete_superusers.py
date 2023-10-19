from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Delete all superusers'

    def handle(self, *args, **options):
        User = get_user_model()
        superusers = User.objects.filter(is_superuser=True)
        superusers.delete()
        self.stdout.write(self.style.SUCCESS('All superusers deleted successfully.'))
