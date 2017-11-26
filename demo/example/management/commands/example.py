
from collections import OrderedDict

from dj.subcommand import CommandWithSubcommands

from django.core.management.base import BaseCommand


class BaseSubcommand(BaseCommand):

    def handle(self, **options):
        self.stdout.write(
            "%s called with options %s"
            % (self.__class__.__name__, options))


class Sub0Command(BaseSubcommand):

    help = "Subcommand with some args"

    def add_arguments(self, parser):
        super(Sub0Command, self).add_arguments(parser)
        parser.add_argument(
            '--sub0-arg1',
            action='store',
            help='Sub0 argument 1')
        parser.add_argument(
            '--sub0-arg2',
            action='store',
            help='Sub0 argument 2')


class Sub1Command(BaseSubcommand):

    help = "Subcommand with compulsory arg"

    def add_arguments(self, parser):
        super(Sub1Command, self).add_arguments(parser)
        parser.add_argument(
            'sub1-arg1',
            action='store',
            default=None,
            help='Sub1 argument 1')
        parser.add_argument(
            '--sub1-arg2',
            action='store',
            default=None,
            help='Sub1 argument 2')


class Sub2Command(BaseSubcommand):

    help = "Subcommand with some choices"

    def add_arguments(self, parser):
        super(Sub2Command, self).add_arguments(parser)
        parser.add_argument(
            '--sub2-arg1',
            action='append',
            choices=map(str, range(0, 10)),
            help='Sub2 argument 1')


class Command(CommandWithSubcommands):

    help = "Command with some sub commands"

    @property
    def subcommands(self):
        return OrderedDict(
            [('sub0', Sub0Command),
             ('sub1', Sub1Command),
             ('sub2', Sub2Command)])
