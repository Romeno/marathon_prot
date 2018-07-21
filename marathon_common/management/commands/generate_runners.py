from django.core.management.base import BaseCommand, CommandError
from marathon_utils.runners_utils import generate_runners
from marathon_runner.models import MarathonRunner


class Command(BaseCommand):
    help = 'generates a CSV file with runners information to be imported into db'

    def add_arguments(self, parser):
        parser.add_argument('--count', nargs='+', default=1000,  type=int, help='Number of runners to generate')

    def handle(self, *args, **options):
        runners = generate_runners(options['count'])
        for r in runners:
            runner = MarathonRunner.from_list(r)
            runner.save()
