from django.core.management.base import BaseCommand, CommandError

import chronotrack as ct

from marathon_chronotrack.models import MarathonRunner
from marathon_marathons.models import Marathon
from marathon_utils.runners_utils import generate_runners


class Command(BaseCommand):
    help = """Pulls data on brackets, timing points, intervals, etc. 
At least 1 marathon should be created and event_id should be set to corresponding Marathon event
"""

    def add_arguments(self, parser):
        # parser.add_argument('--count', default=1000,  type=int, help='Number of runners to fill')
        pass

    def handle(self, *args, **options):
        count = options.get('count')

        cur_marathon = Marathon.objects.filter(is_active=True).last()
        eid = cur_marathon.ct_event_id

        races = ct.races(eid)

