import os
ALLOWED_HOSTS = [host.strip() for host in os.environ.get("ALLOWED_HOSTS", '').split(',')]
ALLOWED_HOSTS = ['localhost']
KONG_ADMIN_URL = os.environ.get('KONG_ADMIN_URL')
KONG_GATEWAY_URL = os.environ.get('KONG_GATEWAY_URL')
KONG_ADMIN_USERNAME = os.environ.get('KONG_ADMIN_USERNAME', None)
KONG_ADMIN_PASSWORD = os.environ.get('KONG_ADMIN_PASSWORD', None)
KONG_PROVISION_KEY = os.environ.get('KONG_PROVISION_KEY')

AUTHENTICATION_BACKENDS = [
    'kong_oauth.authbackends.AppointmentGuruBackend',
    'django.contrib.auth.backends.ModelBackend',
]

KONG_OAUTH_ENDPOINT = 'https://invoiceguru.appointmentguru.co/oauth2/token/'
APPGURU_URL = os.environ.get('APPGURU_URL', 'https://api.appointmentguru.co/')