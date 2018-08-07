import datetime

from django.core.management.base import BaseCommand, CommandError

from marathon_marathons.models import Marathon, MarathonRoute


class Command(BaseCommand):
    help = 'Creates some test data'

    def add_arguments(self, parser):
        # parser.add_argument('--count', default=1000,  type=int, help='Number of runners to fill')
        pass

    def handle(self, *args, **options):
        # count = options.get('count')

        print('Creating test data')

        marathon = Marathon.objects.create(name="Абсолют Московский Марафон",
                                start_time=datetime.datetime(2018, 8, 24, 10, 0, 0),
                                end_time=datetime.datetime(2018, 8, 24, 20, 0, 0),
                                ct_event_id=32804)

        # MarathonRoute.objects.create(marathon=marathon,
        #                              name="10 км",
        #                              start_time=datetime.datetime(2018, 8, 24, 10, 0, 0),
        #                              end_time=datetime.datetime(2018, 8, 24, 12, 0, 0),
        #                              map=
        #                              )

        print('Ready')
