import sys

from django.core.management.base import BaseCommand, CommandError

from marathon_chronotrack import models
from marathon_marathons.models import Marathon, MarathonRoute
from marathon_utils.runners_utils import generate_runners
from marathon_utils.chronotrack import api as ct


class Command(BaseCommand):
    help = """Pulls data on brackets, timing points, intervals, etc. 
At least 1 marathon should be created and event_id should be set to corresponding Marathon event
"""

    def add_arguments(self, parser):
        # parser.add_argument('--count', default=1000,  type=int, help='Number of runners to fill')
        pass

    def handle(self, *args, **options):
        cur_marathon = Marathon.objects.filter(is_active=True).first()
        eid = cur_marathon.ct_event_id

        event = ct.event(eid)

        races = ct.races(eid)
        races = races["event_race"]

        for race in races:
            race_id = int(race["race_id"])

            route = MarathonRoute.objects.filter(ct_race_id=race_id)
            if route:
                route = route.first()
            else:
                # ignore this race if it was not registered manually
                continue

            brackets = ct.brackets(race_id=race_id)
            brackets = brackets["race_bracket"]

            intervals = ct.intervals(race_id=race_id)
            intervals = intervals["race_interval"]

            for bracket in brackets:
                bracket_id = bracket["bracket_id"]
                db_bracket = models.CtBracket.objects.filter(ct_bracket_id=bracket_id)
                if db_bracket:
                    db_bracket = db_bracket.first()
                    db_bracket.name = bracket["bracket_name"]
                    db_bracket.route = route
                    db_bracket.ct_bracket_id = bracket_id
                    db_bracket.save()
                else:
                    models.CtBracket.objects.create(name=bracket["bracket_name"], route=route, ct_bracket_id=bracket_id)

            for interval in intervals:
                interval_id = interval["interval_id"]
                db_interval = models.CtInterval.objects.filter(ct_interval_id=interval_id)
                if db_interval:
                    db_interval = db_interval.first()
                    db_interval.name = bracket["bracket_name"]
                    db_interval.route = route
                    db_interval.ct_interval_id = interval_id
                    db_interval.save()
                else:
                    models.CtInterval.objects.create(name=interval["interval_name"], route=route, ct_interval_id=interval["interval_id"])



