from django.core.management.base import BaseCommand
from oauth.kong import ConsumerResource, ConsumerCredentialResource
import uuid

def get_uuid():
    return str(uuid.uuid4())

def get_or_create_consumer(username, application, secret, custom_id, plugin, with_credentials, **kwargs):
    data= {
        "username": username,
        "custom_id": custom_id
    }
    result = ConsumerResource().create(data)
    res = result.response
    if res.status_code == 409:
        print ('Consumer already exists')
    else:
        user = result.response.json()
        print('******{}******'.format('Consumer:'))
        print(user)
        if with_credentials:
            keys = { "consumer_id": user.get('id'), "plugin": plugin }
            data= {
                "name": application,
                "client_id": user.get('id'),
                "client_secret": secret,
                "redirect_uri": "http://google.com/"
            }
            result = ConsumerCredentialResource().create(keys=keys, data=data)
            print('******{}******'.format('Credentials:'))
            print(result.response.json())


class Command(BaseCommand):
    '''
    usage: createconsumer
    '''
    help = 'Create a consumer in kong (optionally with credentials)'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username')

        parser.add_argument('--application', default=None, help='The application to create')
        parser.add_argument('--custom-id', default=get_uuid(), help='custom id for user')
        parser.add_argument('--plugin', default='oauth2', help='Specify which plugin to create credentials for')
        parser.add_argument('--secret', default=get_uuid(), help='Add a secret to also create credentials')
        parser.add_argument('--with-credentials', default=False, action='store_true', help='should we also create credentials for this user?')

    def handle(self, *args, **options):

        get_or_create_consumer(**options)

        # get_or_create_plugin()

# create_consumer
# create_consumer(anon)
# create_plugin