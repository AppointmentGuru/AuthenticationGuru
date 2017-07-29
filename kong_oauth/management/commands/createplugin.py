from django.core.management.base import BaseCommand
from oauth.kong import GlobalPluginResource
import uuid

def get_uuid():
    return str(uuid.uuid4())

def get_or_create_plugin(provision_key, anonymous_user_id, **kwargs):
    resource = GlobalPluginResource()
    resources = resource.list(**{'verify': False})
    plugins = resources.response.json().get('data', [])

    # create consumers:
    plugin_exists = 'oauth2' in [plugin.get('name') for plugin in plugins]
    if not plugin_exists:
        data = {
            "name": "oauth2",
            "config.provision_key": provision_key,
            "config.enable_password_grant": True,
        }
        if anon_user_id is not None:
            data.update({'config.anonymous': anon_user_id})

        result = resource.create(data)
        if result.status_code == 409:
            print ('oauth plugin already exists')
        else:
            print('******{}******'.format('Oauth details:'))
            print(result.response.json())

    else:
        print('oauth plugin exists')

class Command(BaseCommand):
    help = 'Setup the initial oauth'

    def add_arguments(self, parser):
        # Positional arguments

        # optional
        parser.add_argument('--provision-key', default=get_uuid(), help='Specify a provision_key')
        parser.add_argument('--anonymous-user-id', default=None, help='The user id of the default anonymous user (leave blank to require authentication)')

    def handle(self, *args, **options):

        get_or_create_plugin(**options)

