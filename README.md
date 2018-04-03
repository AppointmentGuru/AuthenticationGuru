# KongOAuth
Simple Django OAuth Backend for Kong

## Installation

```pip install kong-oauth```

## Getting started

You'll need to set the details for connecting to your Kong admin:

In settings.py:

```
KONG_ADMIN_URL = os.environ.get('KONG_ADMIN_URL')
KONG_GATEWAY_URL = os.environ.get('KONG_ADMIN_URL')
# optional if you have oauth:
KONG_ADMIN_USERNAME = os.environ.get('KONG_ADMIN_USERNAME', None)
KONG_ADMIN_PASSWORD = os.environ.get('KONG_ADMIN_PASSWORD', None)

KONG_CLIENT_ID = os.environ.get('KONG_CLIENT_ID')
KONG_CLIENT_SECRET = os.environ.get('KONG_CLIENT_SECRET')

KONG_OAUTH_ENDPOINT = os.environ.get('KONG_OAUTH_ENDPOINT', 'https://46.101.71.132/mockbin/')
APPGURU_URL = os.environ.get('APPGURU_URL', 'https://api.appointmentguru.co/')
```

### Set up Kong:

**Then: let's create an anonomous consumer:**

(optional)

```
python manage.py createconsumer anonomous
```

**Now let's add the plugin**

```
python manage.py createplugin --anonymous-user-id=..
```

* `anonymous-user-id` is the user_id from the anonomous user we created in the previous step
* `provision_key`: you'll need this to perform authentication later

**Now we add a consumer for our API**

```
python manage.py createconsumer joesoap --application=joesawesomeapp --with-credentials
```


**Full example**

```

$ docker-compose run --rm service python manage.py createplugin --anonymous-user-id=fbffe755-eaec-47b5-9c56-a6666deaacbb
...
******Oauth details:******
{'id': 'c993fd0a-6219-486e-96a0-8401362572b9', 'created_at': 1500638477000, 'enabled': True, 'name': 'oauth2', 'config': {'mandatory_scope': False, 'token_expiration': 7200, 'anonymous': 'fbffe755-eaec-47b5-9c56-a6666deaacbb', 'enable_implicit_grant': False, 'hide_credentials': False, 'enable_password_grant': True, 'provision_key': 'function', 'accept_http_if_already_terminated': False, 'global_credentials': False, 'enable_client_credentials': False, 'enable_authorization_code': False}}


******Oauth details:******
{'id': 'fda8e578-6f7b-4ea5-a3cd-c45d8abf286a', 'created_at': 1500638590000, 'enabled': True, 'name': 'oauth2', 'config': {'mandatory_scope': False, 'token_expiration': 7200, 'anonymous': 'fbffe755-eaec-47b5-9c56-a6666deaacbb', 'enable_implicit_grant': False, 'hide_credentials': False, 'enable_password_grant': True, 'provision_key': 'function', 'accept_http_if_already_terminated': False, 'global_credentials': False, 'enable_client_credentials': False, 'enable_authorization_code': False}}


$ docker-compose run --rm service python manage.py createconsumer joesoap --application=joesawesomeapp --with-credentials
...
******Consumer:******
{'custom_id': '5b5b3c80-44cf-498a-b9ce-f39c95f99ba2', 'username': 'joesoap', 'created_at': 1500639019000, 'id': 'accb1e62-5db8-4c74-86fa-5cab232788e0'}
******Credentials:******
{'consumer_id': 'accb1e62-5db8-4c74-86fa-5cab232788e0', 'client_id': 'accb1e62-5db8-4c74-86fa-5cab232788e0', 'id': 'de381dfc-087f-4f72-a104-efc43a8472b9', 'created_at': 1500639019000, 'redirect_uri': ['http://google.com/'], 'name': 'joesawesomeapp', 'client_secret': 'c9a44ec1-73ab-4cc2-ab58-c8b3683c39e6'}
```

### Packaging:

```python setup.py sdist upload```

### Debugging Kong

```
docker exec -ti 990fbb4cdf15 /bin/bash
[root@990fbb4cdf15 /]# tail -f /usr/local/kong/logs/error.log
```