import os

AUTHENTICATION_BACKENDS = [
    'kong_oauth.authbackends.AppointmentGuruBackend',
    'kong_oauth.authbackends.AppointmentGuruOTPBackend',
    'kong_oauth.authbackends.AppointmentGuruPhoneBackend',
]

APPGURU_URL = os.environ.get('APPGURU_URL')
