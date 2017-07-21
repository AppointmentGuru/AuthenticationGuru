import os

AUTHENTICATION_BACKENDS = [
    'kongoauth.authbackends.AppointmentGuruBackend',
]

APPGURU_URL = os.environ.get('APPGURU_URL')
