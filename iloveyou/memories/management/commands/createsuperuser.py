from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    """
    Pulled from here: https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django
    Useful additional command for non-interactively creating a superuser
    Allows for automation of setup
    """
    help = 'Create a superuser, allow password to be provided'

    def add_arguments(self, parser):
        """
        Function to add arguments to the createsuperuser command
        :param parser: The command parser
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--password', dest='password', default=None,
            help='Specifies the password for the superuser.',
        )

    def handle(self, *args, **options):
        """
        Function to handle when a user uses the --password and --username arguments
        :param args: The arguments to be handled
        :param options: The options passed in on the command line
        """
        password = options.get('password')
        username = options.get('username')
        database = options.get('database')

        if password and not username:
            raise CommandError("--username is required if specifying --password")

        super(Command, self).handle(*args, **options)

        if password:
            user = self.UserModel._default_manager.db_manager(database).get(username=username)
            user.set_password(password)
            user.save()
            print("Superuser username: " + username)
            print("Superuser email: " + user.email)
            print("Superuser password: " + password)
