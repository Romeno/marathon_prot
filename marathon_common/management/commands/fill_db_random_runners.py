from django.core.management.base import BaseCommand, CommandError
from marathon_utils.runners_utils import generate_runners
from marathon_runner.models import MarathonRunner


class Command(BaseCommand):
    help = 'Fills the DB with random runners'

    def add_arguments(self, parser):
        parser.add_argument('--count', default=1000,  type=int, help='Number of runners to fill')

    def handle(self, *args, **options):
        count = options.get('count')

        runners = generate_runners(count)
        for r in runners:
            runner = MarathonRunner.from_list(r)
            runner.save()
