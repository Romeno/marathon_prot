import sys

from django.core.management.base import BaseCommand, CommandError

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
        sys.path.insert(0, 'I:\Romeno\Projects\PyCharm\chronotrack')

        import chronotrack as ct

        api = ct.Chronotrack(client_id="b23c9855", user_id="chronotrack@moscowmarathon.org", user_pass="chronodev%77")
        api.set_auth_type(ct.AUTH_SIMPLE)

        cur_marathon = Marathon.objects.filter(is_active=True).first()
        eid = cur_marathon.ct_event_id

        event = api.event(eid)

        races = api.races(eid)

        pass



