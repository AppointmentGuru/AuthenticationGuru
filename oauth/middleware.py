from django.contrib.auth.models import AnonymousUser, User

class KongUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        is_anon = request.META.get('HTTP_X_ANONYMOUS_CONSUMER', False) == 'true'
        user = AnonymousUser()
        if not is_anon:
            user_id = request.META.get('HTTP_X_AUTHENTICATED_USERID', False)
            user = User()
            user.id = user_id
            user.username = user_id
        request.user = user
        response = self.get_response(request)
        return response

"""
{
    "HTTP_X_REAL_IP": "192.168.0.1",
    "HTTP_X_FORWARDED_FOR": "192.168.0.1",
    "HTTP_X_FORWARDED_PROTO": "http",
    "HTTP_X_CONSUMER_ID": "0ee7e34c-ab71-4734-baae-96823bc2ccf7",
    "HTTP_X_CONSUMER_CUSTOM_ID": "admin",
    "HTTP_X_CONSUMER_USERNAME": "admin",
    "HTTP_X_AUTHENTICATED_USERID": "123"
}


{
    "HTTP_X_REAL_IP": "192.168.0.1",
    "HTTP_X_FORWARDED_FOR": "192.168.0.1",
    "HTTP_X_FORWARDED_PROTO": "http",
    "HTTP_X_CONSUMER_ID": "01aae790-5853-4501-b9ea-b33559d2d0e7",
    "HTTP_X_CONSUMER_CUSTOM_ID": "anonomous",
    "HTTP_X_CONSUMER_USERNAME": "anon",
    "HTTP_X_ANONYMOUS_CONSUMER": "true"
}
"""