import sys
import argparse

from django.core.management.base import BaseCommand, CommandError
from marathon_utils.runners_utils import read_runners

from marathon_chronotrack.models import MarathonRunner


class Command(BaseCommand):
    help = 'imports runners from a CSV file into DB'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='File name to import runners from')

    def handle(self, *args, **options):
        file_from = options.get('file')

        runners = read_runners(file_from)
        for r in runners:
            runner = MarathonRunner.from_list(r)
            runner.save()
