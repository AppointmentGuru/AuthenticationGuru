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
