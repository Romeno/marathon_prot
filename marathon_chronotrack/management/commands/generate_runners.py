import sys
import argparse

from django.core.management.base import BaseCommand, CommandError
from marathon_utils.runners_utils import generate_runners, write_runners


class Command(BaseCommand):
    help = 'generates a CSV file with runners\' information to be imported into db'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='File name to write generated info into')
        parser.add_argument('--count', default=1000,  type=int, help='Number of runners to generate')

    def handle(self, *args, **options):
        file = options.get('file')
        if not file:
            file = sys.stdout
        count = options.get('count')

        runners = generate_runners(count)
        write_runners(runners, file)

