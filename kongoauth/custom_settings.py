import os
ALLOWED_HOSTS = [host.strip() for host in os.environ.get("ALLOWED_HOSTS", '').split(',')]

KONG_ADMIN_URL = os.environ.get('KONG_ADMIN_URL')
KONG_GATEWAY_URL = os.environ.get('KONG_GATEWAY_URL')
KONG_ADMIN_USERNAME = os.environ.get('KONG_ADMIN_USERNAME', None)
KONG_ADMIN_PASSWORD = os.environ.get('KONG_ADMIN_PASSWORD', None)
KONG_PROVISION_KEY = os.environ.get('KONG_PROVISION_KEY')

AUTHENTICATION_BACKENDS = [
    'kong_oauth.authbackends.AppointmentGuruBackend',
    'kong_oauth.authbackends.AppointmentGuruOTPBackend',
    'kong_oauth.authbackends.AppointmentGuruPhoneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

KONG_CLIENT_ID = "1E10898B-9D2F-43E3-838A-56E203A6EE38"
KONG_CLIENT_SECRET = "D657BFCB-F7ED-47A5-A976-D47D57540409"

# KONG_OAUTH_ENDPOINT = 'https://invoiceguru.appointmentguru.co/oauth2/token/'
KONG_OAUTH_ENDPOINT = os.environ.get('KONG_OAUTH_ENDPOINT')
APPGURU_URL = os.environ.get('APPGURU_URL', 'https://api.appointmentguru.co/')