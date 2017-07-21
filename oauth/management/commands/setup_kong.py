from django.core.management.base import BaseCommand
from oauth.kong import GlobalPluginResource, GlobalConsumerResource, ConsumerCredentialResource
import uuid

def get_uuid():
    return str(uuid.uuid4())

def get_or_create_consumer(username, custom_id):
    data= {
        "username": username,
        "custom_id": custom_id
    }
    result = GlobalConsumerResource().create(**data)

def get_or_create_plugin(anon):
    resource = GlobalPluginResource()
    resources = resource.list(**{'verify': False})
    plugins = resources.response.json().get('data', [])

    # create consumers:
    plugin_exists = 'oauth2' in [plugin.get('name') for plugin in plugins]
    if not plugin_exists:
        data = {
            "name": "oauth2",
            "config.enable_password_grant": True,
            "config.anonomous": anon.get('id')
        }
        resource.create(data)
    else:
        print('oauth plugin exists')

class Command(BaseCommand):
    help = 'Setup the initial oauth'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username')
        parser.add_argument('secret', default=False, help='Add a secret to also create credentials')
        parser.add_argument('--custom-id', default=get_uuid(), help='custom id for user')

        parser.add_argument('--allow-anon', default=True, help='Allow anonomous access'
        )

    def handle(self, *args, **options):
        import ipdb;ipdb.set_trace()
        # get_or_create_consumer()

        # get_or_create_plugin()

