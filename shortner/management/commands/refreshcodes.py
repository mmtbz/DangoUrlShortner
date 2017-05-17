__author__ = 'Dave'

from django.core.management.base import BaseCommand, CommandError
from shortner.models import RawURL


class Command(BaseCommand):
    help = 'Refreshes all RawURL shortcodes'

    # def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return RawURL.m.refresh_shortcode()
